from ast import keyword
from distutils.command.build_scripts import first_line_re
from operator import truediv
from warnings import catch_warnings
from analyzers import dtoscillator
from numpy import column_stack
from test import get_data
import numpy as np
from scipy.signal import argrelextrema
import pandas as pd
import matplotlib.pyplot as plt
from analyzers import rsi
import time
from test import get_data

ohlc = get_data('BTC-USDT', timeframe='1h',limit=200)

num = pd.DataFrame()
minima = pd.DataFrame()
rsiss = pd.DataFrame()
# num['num'] = pd.DataFrame(argrelextrema(ohlc.Low.values, np.less_equal,order=1)[0])
maxima = pd.DataFrame(ohlc.iloc[argrelextrema(ohlc.Close.values, np.greater_equal,order=1)[0]].Close)
minima = pd.DataFrame(ohlc.iloc[argrelextrema(ohlc.Close.values, np.less_equal,order=1)[0]].Close)
# print(argrelextrema(ohlc.values, np.greater_equal,order=5)[0])
# print(argrelextrema(ohlc.values, np.less_equal,order=5)[0])
# print(minima['max'])
# print(minima['min'])
# plt.scatter(minima.index,minima['min'],c='r')
# plt.scatter(minima.index,minima['max'],c='g')
max_min = pd.concat([maxima, minima]).sort_index()
plt.scatter(max_min.index,max_min,c='g')
plt.plot(ohlc.index,ohlc.Close)
patterns = []
for i in range(5, max_min.shape[0]):  
        window = max_min.iloc[i-5:i]
        
        # Pattern must play out in less than n units
        # if window.index[-1] - window.index[0] > 100:      
        #     continue   
        # print(window)    
        a = window.Close[0]
        b = window.Close[1]
        c = window.Close[2]
        d = window.Close[3]
        e = window.Close[4]
                
        # IHS
        if a<b and c<a and c<e and c<d and e<d and abs(b-d)<=np.mean([b,d])*0.02:
               patterns.append(window)
df = pd.DataFrame(patterns)
print(df)

