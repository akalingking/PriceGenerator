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

#http://stackoverflow.com/questions/4542352/import-from-sibling-directory
import os
import inspect

g_is_initialized = False

def set_path():
    global g_is_initialized
    if (g_is_initialized is False):
        g_is_initialized = True 
        try:
            parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            os.sys.path.insert(0,parentdir) 
        except:
            currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
            parentdir = os.path.dirname(currentdir)
        os.sys.path.insert(0,parentdir) 