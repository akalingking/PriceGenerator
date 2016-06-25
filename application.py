'''
https://opensource.org/licenses/MIT

License: The MIT License (MIT)

Copyright (c) 2016 Ariel Kalingking akalingking@gmail.com

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
'''
import ConfigParser
from applicationbase import ApplicationBase
from websocket.wsserver import WsServer
import numpy as np
import datetime
from threading import RLock, Condition
import os

from frequency import Frequency
from symbols import Symbols
from tradeitem import TradeItem
from generator.gbm import GBM
import logger

class Application(ApplicationBase):
    application_name = None
    
    def __init__(self, address=None, port=None, configFile=None, logFile=None):
        ApplicationBase.__init__(self)
        self.frequency_ = Frequency.Minute
        self.lock_ = RLock()
        self.cond_ = Condition(self.lock_)
        self.current_price_ = {}
        self.current_volume_ = {}
        self.run_ = False
        self.enable_ws_ = True
        self.wsserver_ = None
        self.isdaemon_ = False
        self.loglevel_ = logger.logging.DEBUG
        
        if (Application.application_name != None):
            self.pidfile_path = "/tmp/" + Application.application_name+".pid"
#             self.pidfile_path = "/var/run/" + Application.application_name+".pid"
        
        if (logFile is None):
            self.logfile_ = "/tmp/" + Application.application_name+".log"
#             self.logfile_ = "/var/log/" + Application.application_name+".log"
        else:
            self.logfile_ = logFile
        
        if (address == None):
            self.address_ = '127.0.0.1'
        else:
            self.address_ = address    
        if (port == None):
            self.port_ = 9000
        else:
            self.port_ = port
            
        if (address is None and port is None):
            if (configFile is None):
                if (Application.application_name is not None):
                    self.configfile_ = Application.application_name + ".cfg"
                else:
                    self.configfile_ = "application.cfg"
            else:
                self.configfile_ = configFile
        else:
            self.configfile_ = None
                   
    def read_config(self, configFile):
#         print("Application.read_config_ file='%s'" % configFile)
        try:
            self.config_ = ConfigParser.SafeConfigParser()
            abs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './', self.configfile_)
            self.config_.read(abs_path)
            self.address_ = self.config_.get("root", "address")
            self.port_ = self.config_.getint("root", "port")
            self.enable_ws_ = self.config_.getboolean("root", "enablews")
        except ConfigParser.Error as e:
            print("Application.read_config_ exception='%s'" % str(e))
        
    def start(self):
        if (self.configfile_ is not None):
            self.read_config(self.configfile_)
        
        logManager = logger.LogManager(self.logfile_,self.loglevel_)
        self.logger_ = logManager.getLogger(Application.application_name)
            
        if (self.enable_ws_):
            self.wsserver_ = WsServer(self.address_, self.port_)
            self.wsserver_.start()
        
        ret = True
        if (self.isdaemon_ is False):
            ret = ApplicationBase.start(self)
        
        return ret
    
    def stop(self):
        if (self.enable_ws_ and self.wsserver_ is not None):
            self.wsserver_.stop()
            
        ret = ApplicationBase.stop(self)
        
        self.cond_.acquire()
        self.cond_.notify_all()
        self.cond_.release()
        
        return ret
        
    def do_work_(self):
        self.log().debug("Application::do_work_ start")
        
        while (self.is_run_):
            keys = Symbols.symbols.keys()
            for key in keys:
#                 self.log().info("Application::do_work_ processing '%s'", key)
                item = TradeItem()
                   
                tradeStat = Symbols.trades[key]
                  
                # generate the trade data OHLC
                trades = np.zeros(4)
                for i in np.arange(0, 4):
                    # use daily volaitlity not the intraday
                    gen = GBM(1, Frequency.Day)
                      
                    current_price = 0.0
                    if (self.current_price_.has_key(key)):
                        current_price = self.current_price_[key]
                    else:
                        current_price = Symbols.trades[key].start_value
                      
                    trades[i] = gen.get_next_value(
                        tradeStat.mean, 
                        tradeStat.std,
                        current_price)
                    
                item.Symbol = key
                item.Low = min(trades)
                item.High = max(trades)
                item.Open = trades[0]
                item.Close = trades[3]
                  
                self.current_price_[key]=item.Close
                  
                volume_stat = Symbols.volumes[key]
                gen = GBM(1, Frequency.Day)
                current_volume = None
                if (self.current_volume_.has_key(key)):
                    current_volume = self.current_volume_[key]
                else:
                    current_volume = volume_stat.start_value
                
                # generate volume
                item.Volume = gen.get_next_value(
                    volume_stat.mean, 
                    volume_stat.std,
                   current_volume)
                 
                # generate data
                item.Date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M.%S")
                
                self.current_volume_[key] = item.Volume
                
                self.log().info("%s", item.__str__())
                
                if (self.enable_ws_):
                    self.wsserver_.send(item.__str__())
                 
            self.cond_.acquire()
            self.cond_.wait(timeout=self.frequency_)
            self.cond_.release()
        
        self.log().debug("Application::do_work_ stop")
