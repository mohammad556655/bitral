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
from forex_getdata import get_data

def find_pos_rsi_div(pair,timeframe,ohlc):
    rsis = rsi.RSI()
    rsi_values = rsis.analyze(ohlc, 14)

    num = pd.DataFrame()
    minima = pd.DataFrame()
    rsiss = pd.DataFrame()
    num['num'] = pd.DataFrame(argrelextrema(ohlc.Low.values, np.less_equal,order=1)[0])
    minima['min'] = pd.DataFrame(ohlc.iloc[argrelextrema(ohlc.Low.values, np.less_equal,order=1)[0]].Low)
    rsiss['rsi'] = pd.DataFrame(rsi_values.iloc[argrelextrema(ohlc.Low.values, np.less_equal,order=1)[0]].rsi)
    minima = minima.reset_index()
    rsiss = rsiss.reset_index()
    # print(num)
    # print(minima)
    # print(rsiss)
    # plt.scatter(minima.index,minima,c='r')
    # plt.plot(ohlc.index,ohlc.Low)
    # plt.show()

    def linear_formula(x, y1, y2, x2):
        m = (y2 - y1) / x2
        y = m * x + y1
        return y


    positive_dive = pd.DataFrame()

    for n1 in range(0, minima.shape[0] - 1):
        for n2 in range(n1 + 1, minima.shape[0]):
            if minima['min'][n1] > minima['min'][n2] and rsiss['rsi'][n1] < rsiss['rsi'][n2]:

                low1 = minima['min'][n1]
                low2 = minima['min'][n2]

                rsi1 = rsiss['rsi'][n1]
                rsi2 = rsiss['rsi'][n2]

                num1 = num['num'][n1]
                num2 = num['num'][n2]
                date1 = minima['Date'][n1]
                date2 = minima['Date'][n2]
                count = abs(num2 - num1)
                # print(num1)
                # print(num2)
                # print(count)
                # print(f"date1 {date1}")
                # print(f"date2 {date2}")
                # print(f"low1 {low1}")
                # print(f"low2 {low2}")
                # print(f"rsi1 {rsi1}")
                # print(f"rsi2 {rsi2}")
                is_div_low = True
                is_div_rsi = True

                for i in range(0, count + 1):
                    value_low = linear_formula(i, y1=low1, y2=low2, x2=count)
                    value_rsi = linear_formula(i, y1=rsi1, y2=rsi2, x2=count)
                    position = num1 + i
                    # print(f'pisition {position} and ohlc {ohlc.Low[position]}')
                    # print(f"low value {value_low}")
                    # print(f"rsi value {value_rsi}")
                    if ohlc.Low[position] < value_low:
                        is_div_low = False
                        break
                    if rsi_values.rsi[position] < value_rsi:
                        is_div_rsi = False
                        break
                if (is_div_low == True and is_div_rsi == True):
                    # print(f"low1 value {low1} and low2 {low2}")
                    # print(f"rsi1 value {rsi1} and rsi2 value {rsi2}")
                    div1 = low1
                    div2 = low2
                    temp = pd.DataFrame([[date1, div1, date2, div2]],columns=['date1', 'div1', 'date2', 'div2'])
                    positive_dive = pd.concat([positive_dive, temp])
    return positive_dive
