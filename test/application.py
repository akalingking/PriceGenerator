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
from application import Application
import sys

app_instance = None

def main():
    Application.application_name = "application"
    
    print("start '%s'", sys.argv[0])
    
    #app_instance = Application("127.0.0.1", 9000)
    app_instance = Application()
      
    try:
        app_instance.start()
        app_instance.wait(10)
    except Exception as e:
        app_instance.log().info("Application.Main exception %s", str(e))
    finally:
        app_instance.stop()
          
    app_instance.log().info("stop '%s'", sys.argv[0])

if __name__=="__main__":
    main()
