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
from __set_path import set_path
set_path()
from applicationbase import ApplicationBase
from time import sleep

if __name__=="__main__":
    class ApplicationTest(ApplicationBase):
        def do_work_(self):
            print "ApplicationTest.do_work_ start"
            for i in range(5):
                print "ApplicationTest.do_work_ %d" % i 
                sleep(5)
            self.stop()
            print "ApplicationTest.do_work_ stop"
              
    print "main start"      
    try:
        application = ApplicationTest()
        application.start()
        application.wait()
    except KeyboardInterrupt:
        application.stop()
    print "main stop"    

'''
from frequency import Frequency
from symbols import Symbols
from tradeitem import TradeItem
from generator.gbm import GBM
import numpy as np
import datetime
import logger
from threading import Thread, Lock, RLock, Condition
import signal, os, sys, time, logging
 
class ApplicationTest(ApplicationBase):
    def __init__(self):
        ApplicationBase.__init__(self)
        self.frequency_ = Frequency.Second
        self.lock_ = RLock()
        self.cond_ = Condition(self.lock_)
        self.current_price_ = {}
        self.current_volume_ = {}
     
    def do_work_(self):
        print "ApplicationTest.do_work_ start"
         
        while (self.is_run_):
            keys = Symbols.symbols.keys()
            for key in keys:
                print "ApplicationTest.do_work_ processing '%s'" % key
                item = TradeItem
                   
                symbol = Symbols.symbols[key]
                   
                tradeStat = Symbols.trades[key]
                   
                # generate the trade data OHLC
                trades = np.zeros(4)
                for i in np.arange(0, 4):
                    gen = GBM(1, self.frequency_)
                       
                    current_price = 0.0
                    if (self.current_price_.has_key(key)):
                        current_price = self.current_price_[key]
                       
                    trades[i] = gen.get_next_value(
                        tradeStat.mean, 
                        tradeStat.std,
                        current_price)
                   
                item.Symbol = symbol.code
                item.Low = min(trades)
                item.High = max(trades)
                item.open = trades[0]
                item.close = trades[3]
                   
                self.current_price_[key]=item.close
                   
#                 volumeStat = Symbols.volumes[key]
#                   
#                 gen = GBM(1, self.frequency_)
                   
                item.Volume = 10000
                   
                item.date = datetime.datetime.now()
                   
                self.current_volume_[key] = item.Volume
                   
                self.log().debug("Symbol:%s Open:%f High:%f Low:%f Close:%f Volume:%f",
                    item.Symbol, item.Open, item.High, item.Low, item.Close, item.Volume)
             
            break      
#             self.cond_.acquire()
#             self.cond_.wait(self.frequency_)
#             self.cond_.acquire()
         
        self.log().debug("Application::do_work_ stop")
         
#@{test
def main():
    app_instance = ApplicationTest()
 
    app_instance.log().info("start '%s'", sys.argv[0])
       
    try:
        app_instance.start()
        app_instance.wait()
    except Exception as e:
        app_instance.log().info("Exception %s", str(e))
    finally:
        app_instance.stop()
           
    app_instance.log().info("stop '%s'", sys.argv[0])
 
if __name__=="__main__":
    main()
'''