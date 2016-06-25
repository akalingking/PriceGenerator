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
from numpy import std

class Symbols(object):
    class Symbol(object):
        def __init__(self, symbol, code, name):
            self.symbol = symbol
            self.code = code
            self.name = name
    class Trade(object):
        def __init__(self, start, mean, std):
            self.start_value = start
            self.mean = mean
            self.std = std
    class Volume(object):
        def __init__(self, start, mean, std):
            self.start_value = start
            self.mean = mean
            self.std = std
    
    symbols = {
        "BDO":  Symbol("BDO", 1, "Banco De Oro"),
#         "BPI":  Symbol("BPI", 2, "Bank of the Philippine Islands"),
#         "AC":   Symbol("AC", 3, "Ayala Corporation"),
        }
    
    trades = {
        "BDO":  Trade(250, 230, 0.15),
#         "BPI":  Trade(700, 650, 0.07),
#         "AC":   Trade(700, 650, 0.07),
        }
    
    volumes = {
        "BDO":  Volume(1000, 900, 0.15),
#         "BPI":  Volume(1000, 1000, 0.07),
#         "AC":   Volume(1000, 950, 0.05),
        }

# print "bdo='%s'" % Symbols.symbols["BDO"].code