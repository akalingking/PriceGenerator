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
from daemonrunner import runner
from application import Application
from daemonrunner import DaemonRunner
import signal

g_daemon = None

def signal_handler(signum, frame):
    global g_daemon
    g_daemon.app.application.log().info('Signal handler called with signal %d', signum)
    g_daemon.app.application.stop()
 
    
class Application_():
    def __init__(self, address=None, port=None, configFile=None):
        self.application = Application(address=address, port=port, configFile=configFile)
        Application.application_name = "pricegenerator"
        pidfile = self.application.application_name + ".pid"
        # fields required by DaemonRunner
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/' + pidfile
        self.pidfile_timeout = 5
        self.foreground = False
        
        self.application.is_run_ = True
        self.application.isdaemon_ = True
          
    def run(self):
        self.application.start()
        self.application.do_work_()
        
            
def main():
    global g_daemon
    
    Application.application_name = "pricegenerator"
    
    app = Application_()

    g_daemon = DaemonRunner(app)   
    
    if app.foreground:
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGILL, signal_handler)
        signal.signal(signal.SIGHUP, signal_handler)
        
        try:
            app.application.isdaemon_ = False
            app.application.start()
            app.application.wait()
        except KeyboardInterrupt:
            app.application.log().info("console interrupt!")
        except Exception as e:
            app.application.log().info("Exception %s", str(e))
        finally:
            app.application.stop()
    else:
        g_daemon.daemon_context.signal_map = {
            signal.SIGTERM: signal_handler,
            signal.SIGINT: signal_handler,
            signal.SIGILL: signal_handler,
            signal.SIGHUP: signal_handler,
        }
        
        try:
            g_daemon.do_action()
        except runner.DaemonRunnerStopFailureError as e:
            print ("error stopping '%s', process might be in foreground" % str(e))
        except runner.DaemonRunnerStartFailureError as e:
            print ("error starting e='%s'" % str(e))
        except runner.DaemonRunnerError as e:
            print ("error e='%s'" % str(e))
          
                 
if __name__ == "__main__":
    main()
