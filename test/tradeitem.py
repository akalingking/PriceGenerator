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
from tradeitem import TradeItem
import datetime
import dicttoxml

#@{Test
if __name__=="__main__":        
    item = TradeItem()
    item.Symbol = "BDO"
    item.Date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M.%S")
    item.Open = 1.0
    item.High = 1.0
    item.Low = 1.0
    item.Close = 1.0
    item.Volume = 10.0
    
#     print '%s' % item.__dict__
    print '%s' % dicttoxml.dicttoxml(item.__dict__, attr_type=False)
    
#@}Test    