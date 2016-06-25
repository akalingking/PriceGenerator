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
class TradeItem(object):
    __slots__ = ["Date","Symbol","Open","High","Low","Close","Volume"]
    def __init__(self,date=None, symbol=None, o=None, h=None, l=None, c=None, v=None):
        self.Date = date
        self.Symbol = symbol
        self.Open = o
        self.High = h
        self.Low = l
        self.Close = c
        self.Volume = v
    
    @property
    def __dict__(self):
        return {s: getattr(self, s) for s in self.__slots__ if hasattr(self, s)}
    
    def __str__(self):
        fields = "Date=" + self.Date
        fields += ",Symbol=" + self.Symbol
        fields += ",Open=" + ("%0.3f" % self.Open)
        fields += ",High=" + ("%0.3f" % self.High)
        fields += ",Low=" + ("%0.3f" % self.Low)
        fields += ",Close=" + ("%0.3f" % self.Close)
        fields += ",Volume=" + ("%0.3f" % self.Volume)
        return fields
        