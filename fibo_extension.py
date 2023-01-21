from unittest import result
import matplotlib.pyplot as plt
from test import get_data
from analyzers import adx
from scipy.signal import argrelextrema
import numpy as np
import pandas as pd
pairs=['BTC-USDT']
for pair in pairs:
    ohlc = get_data(pair,timeframe='1h')
    maxima = pd.DataFrame()
    minima = pd.DataFrame() 
    nlargest = pd.DataFrame()
    nsmallest = pd.DataFrame()
    maxima['max'] = pd.DataFrame(ohlc.iloc[argrelextrema(ohlc.High.values, np.greater_equal,order=2)[0]].High)
    minima['min'] = pd.DataFrame(ohlc.iloc[argrelextrema(ohlc.Low.values, np.less_equal,order=2)[0]].Low)
    ohlc = ohlc.reset_index()
    min=ohlc['Close'].min()
    idmin = ohlc['Close'].idxmin()
    
    max = ohlc[idmin:]['Close'].max()
    idmax = ohlc[idmin:]['Close'].idxmax()

    min2 = ohlc[idmax:]['Close'].min()
    idmin2 = ohlc[idmax:]['Close'].idxmin()
    print(min)
    print(max)
    print(min2)

    # plt.scatter(nlargest.index,nlargest,c='r')
    # plt.plot(ohlc.index,ohlc.Close)
    # plt.show()
    maximum_price = max
    minimum_price = min
    minimum_price2 = min2
    difference1 = maximum_price - minimum_price
    difference2 = maximum_price - minimum_price2

    first_level = maximum_price +difference1 * 0.236
    second_level = maximum_price +difference1 * 0.382
    third_level = maximum_price +difference1 * 0.5
    fourth_level = maximum_price +difference1 * 0.618 

    first_level = first_level - difference2
    second_level = second_level - difference2
    third_level = third_level - difference2
    fourth_level = fourth_level - difference2 

    print(first_level)
    print(second_level)
    print(third_level)
    print(fourth_level)