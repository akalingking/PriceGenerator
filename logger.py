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
import logging
from logging import handlers
import threading

class Singleton_mc(type):
    def __init__(cls, name, bases, dict):
        super(Singleton_mc,cls).__init__(name, bases, dict)
        
        cls_new = cls.__new__
        
        # works like lambda
        def __new(cls,*args,**kwds):
            if cls.instance == None:
                cls.instance = cls_new(cls,*args,**kwds)
            return cls.instance
        
        cls.instance = None
        cls.__new__ = staticmethod(__new)


# This formatter provides a way to hook in formatTime.
class Formatter(logging.Formatter):
    DATETIME_HOOK = None

    def formatTime(self, record, datefmt=None):
        newDateTime = None

        if Formatter.DATETIME_HOOK is not None:
            newDateTime = Formatter.DATETIME_HOOK()

        if newDateTime is None:
            ret = logging.Formatter.formatTime(self, record, datefmt)
        else:
            ret = str(newDateTime)
        return ret        
        
        
class LogManager(object):
    __metaclass__ = Singleton_mc
    rootLoggerInitialized = False
    def __init__(self, 
        file_log=None, 
        level=logging.INFO, 
        console_log=True,
        log_format="%(asctime)s %(name)s [%(levelname)s] %(message)s") :
        self.initLock = threading.Lock()
        self.log_format = log_format 
        self.level = level
        self.file_log = file_log  # File name
        self.console_log = console_log

    def init_handler(self, handler):
        handler.setFormatter(Formatter(self.log_format))

    def init_logger(self, logger):
        logger.setLevel(self.level)

        if self.file_log is not None:
            self.fileHandler = handlers.RotatingFileHandler(self.file_log, maxBytes=1024*1024*5, backupCount=5)
            self.init_handler(self.fileHandler)
            logger.addHandler(self.fileHandler)
    
        if self.console_log:
            consoleHandler = logging.StreamHandler()
            self.init_handler(consoleHandler)
            logger.addHandler(consoleHandler)

    def initialize(self):
        with self.initLock:
            if not LogManager.rootLoggerInitialized:
                self.init_logger(logging.getLogger())
                LogManager.rootLoggerInitialized = True
    
    def getLogger(self, name=None):
        self.initialize()
        return logging.getLogger(name)
