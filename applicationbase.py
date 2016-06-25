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
import abc
from _pyio import __metaclass__
from threading import Thread, RLock, Condition

class ApplicationBase(Thread):
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        Thread.__init__(self)
        self.logger_ = None
        self.loglevel_ = None
        self.lock_stop_ = RLock()
        self.cond_stop_ = Condition(self.lock_stop_)
        self.lock_run_ = RLock()
        self.is_run_ = False
        self.wait_ = None
        
    @abc.abstractmethod
    def do_work_(self):
        raise NotImplementedError
        
    def run(self):
        print("Application.run start")
        
        with self.lock_run_:
            while (self.is_run_):
                    self.do_work_()
                    
        with self.lock_stop_:
            self.cond_stop_.notify_all()
            
        print("Application.run stop")    
        
    def start(self):
        with self.lock_run_:
            self.is_run_ = True
            Thread.start(self)
        
    def stop(self):
        with self.lock_run_:
            if (self.is_run_):
                self.is_run_ = False
        print "ApplicationBase.stop is_run_=", self.is_run_
            
    def wait(self, wait=None):
        with self.lock_stop_:
            while(self.is_run_):
                self.cond_stop_.wait(wait)
        
    def log(self):
        return self.logger_
