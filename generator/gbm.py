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
#import ast
#import dateutil
#import pandas.core.datetools as datetools
# import pandas as pd
import numpy as np
import random
from scipy import stats
from frequency import Frequency

class GBM(object):
    DAYSINYEAR = 252
    HOURSINYEAR = DAYSINYEAR*8
    MINUTESINYEAR = HOURSINYEAR*60
    SECONDSINYEAR = MINUTESINYEAR*60
    
    #@ interval is in days
    #@ 1 min frequency is 1/60*24
    def __init__(self, interval=1.0, freq=Frequency.Day):
        self.__frequency = freq
        
        if (self.__frequency == Frequency.Day):
            self.__interval = float((interval*1.0)/GBM.DAYSINYEAR)
        elif (self.__frequency == Frequency.Hour):
            self.__interval = float((interval*1.0)/GBM.HOURSINYEAR)
        elif (self.__frequency == Frequency.Minute):
            self.__interval = float((interval*1.0)/GBM.MINUTESINYEAR)
        elif (self.__frequency == Frequency.Second):
            self.__interval = float((interval*1.0)/GBM.SECONDSINYEAR)
                 
#         print ("interval %f" % self.__interval)

    def __getRandom(self):
        return random.random()

    def get_next_value(self, mean, std, currValue):
        #print ("GBM.get_next_value m=%.3f s=%.3f c=%.3f" % (mean,std,currValue))
        # Geometric Brownian Motion
        #       return =  drift + shock
        #         dS_t =  u d_t  +  sigma dW_t
        #  S_t - S_t-1 = u d_t  +  sigma dW_t
        #          S_t = S_t-1 + u d_t  +  sigma dW_t
        next_value = 0.0
        drift = mean * self.__interval
        shock = std * stats.norm.ppf(self.__getRandom()) * np.sqrt(self.__interval)
        next_value = currValue + drift + shock
        return next_value

