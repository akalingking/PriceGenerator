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
import logging
import logger

if __name__=="__main__":
    #done once
    log1 = logger.LogManager(level=logging.DEBUG)
    
    logger1 = log1.getLogger("test1")
    logger1.info("this is a test1")
    logger1.debug("this is a debug test1")
#     print(logger1)
    log2 = logger.LogManager(level=logging.DEBUG)
    logger2 = log2.getLogger("test2")
#     print (logger2)
    logger2.info("this is a test2")
    logger2.debug("this is a debug test2")
    
    log3 = logger.LogManager()
    logger3 = log3.getLogger("test3")
    logger3.info("this is a test3")
    logger3.debug("this is a debug test3")
#
#     logger3 = Logger().getLogger("test3")
#     logger3.info("this is a test3")
   