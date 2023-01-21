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

ohlc = get_data('ETH-USDT','15m',limit=200)

rsis = rsi.RSI()
rsi_values = rsis.analyze(ohlc, 14)

num = pd.DataFrame()
maxima = pd.DataFrame()
rsiss = pd.DataFrame()
num['num'] = pd.DataFrame(argrelextrema(ohlc.High.values, np.greater_equal,order=1)[0])
maxima['max'] = pd.DataFrame(ohlc.iloc[argrelextrema(ohlc.High.values, np.greater_equal,order=1)[0]].High)
rsiss['rsi'] = pd.DataFrame(rsi_values.iloc[argrelextrema(ohlc.High.values, np.greater_equal,order=1)[0]].rsi)
maxima = maxima.reset_index()
rsiss = rsiss.reset_index()
print(num)
print(maxima)
print(rsiss)
# plt.scatter(minima.index,minima,c='r')
# plt.plot(ohlc.index,ohlc.Low)
# plt.show()
def linear_formula(x,y1,y2,x2):
    m = (y2-y1)/x2
    y = m*x + y1
    return y


negative_dive = pd.DataFrame()
for n1 in range(0,maxima.shape[0]-1):
    for n2 in range(n1+1,maxima.shape[0]):
        if maxima['max'][n1]< maxima['max'][n2] and rsiss['rsi'][n1]> rsiss['rsi'][n2]:
            # print(maxima_pd.num[n1])
            # print(maxima_pd.num[n2])

            high1 = maxima['max'][n1]
            high2 = maxima['max'][n2]

            rsi1 = rsiss['rsi'][n1]
            rsi2 = rsiss['rsi'][n2]

            num1 = num['num'][n1]
            num2 = num['num'][n2]
            count = abs(num2-num1)
            date1 = maxima['Date'][n1]
            date2 = maxima['Date'][n2]
            # print(num1)
            # print(num2)
            # print(count)
            # print(f"date1 {date1}")
            # print(f"date2 {date2}")
            # print(f"high1 {high1}")
            # print(f"high2 {high2}")
            # print(f"rsi1 {rsi1}")
            # print(f"rsi2 {rsi2}")
            is_div_high = True
            is_div_rsi = True

            for i in range(0 ,count+1):
                value_high = linear_formula(i,y1=high1 ,y2=high2 ,x2=count)
                value_rsi = linear_formula(i, y1=rsi1, y2=rsi2, x2=count)
                position = num1+i
                # print(f'pisition {position} and ohlc {ohlc.high[position]}')
                # print(f"low value {value_high}")
                # print(f"rsi value {value_rsi}")
                if ohlc.High[position] > value_high:
                    is_div_high = False
                    # print("ohlc fault")
                    break
                if rsi_values.rsi[position] > value_rsi:
                    is_div_rsi = False
                    # print("rsi fault")
                    break
            if(is_div_rsi==True and is_div_high==True):
                print(f"low1 value {high1} and low2 {high2}")
                print(f"rsi1 value {rsi1} and rsi2 value {rsi2}")
                date1 = maxima['Date'][n1]
                date2 = maxima['Date'][n2]
                div1 = high1
                div2 = high2
                temp = pd.DataFrame([[date1,div1,date2,div2]],columns=['date1','div1','date2','div2'])
                negative_dive = pd.concat([negative_dive,temp])
                print(negative_dive)
