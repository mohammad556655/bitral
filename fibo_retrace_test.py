from unittest import result
import matplotlib.pyplot as plt
from test import get_data
from analyzers import adx
from scipy.signal import argrelextrema
import numpy as np
import pandas as pd
pairs=['AXS-USDT']
for pair in pairs:
    ohlc = get_data(pair,timeframe='1h')
    highest_swing = -1
    lowest_swing = -1
    for i in range(1,ohlc.shape[0]-1):
        if ohlc['High'][i] > ohlc['High'][i-1] and ohlc['High'][i] > ohlc['High'][i+1] and (highest_swing == -1 or ohlc['High'][i] > ohlc['High'][highest_swing]):
                highest_swing = i
        if ohlc['Low'][i] < ohlc['Low'][i-1] and ohlc['Low'][i] < ohlc['Low'][i+1] and (lowest_swing == -1 or ohlc['Low'][i] < ohlc['Low'][lowest_swing]):
            lowest_swing = i
    ratios = [0,0.236, 0.382, 0.5 , 0.618, 0.786,1]
    colors = ["black","r","g","b","cyan","magenta","yellow"]
    levels = []
    max_level = ohlc['High'][highest_swing]
    min_level = ohlc['Low'][lowest_swing]
    for ratio in ratios:
        if highest_swing > lowest_swing: # Uptrend
            levels.append(max_level - (max_level-min_level)*ratio)
        else: # Downtrend
            levels.append(min_level + (max_level-min_level)*ratio)
    plt.rcParams['figure.figsize'] = [12, 7]
    plt.rc('font', size=14)
    plt.plot(ohlc['Close'])
    start_date = ohlc.index[min(highest_swing,lowest_swing)]
    end_date = ohlc.index[max(highest_swing,lowest_swing)]
    for i in range(len(levels)):
        plt.hlines(levels[i],start_date, end_date,label="{:.1f}%".format(ratios[i]*100),colors=colors[i], linestyles="dashed")
    plt.legend()
    plt.show()