from unittest import result
import matplotlib.pyplot as plt
from test import get_data
from analyzers import adx
from scipy.signal import argrelextrema
import numpy as np
import pandas as pd

def find_fib_up(ohlc,min):
    max=ohlc['Close'].max()

    print(min)
    print(max)

    # plt.scatter(nlargest.index,nlargest,c='r')
    # plt.plot(ohlc.index,ohlc.Close)
    # plt.show()
    maximum_price = max
    minimum_price = min
    difference = maximum_price - minimum_price
    first_level = maximum_price - difference * 0.236
    second_level = maximum_price - difference * 0.382
    third_level = maximum_price - difference * 0.5
    forth_level = maximum_price - difference * 0.618 
    fifth_level = maximum_price - difference * 0.786 
    return {'y0.236':first_level, 'y0.382':second_level, 'y0.5':third_level, 'y0.618':forth_level,'y0.786':fifth_level}


def find_fib_down(ohlc,max):
    min=ohlc['Close'].min()

    print(min)
    print(max)

    # plt.scatter(nlargest.index,nlargest,c='r')
    # plt.plot(ohlc.index,ohlc.Close)
    # plt.show()
    maximum_price = max
    minimum_price = min
    difference = maximum_price - minimum_price
    first_level = minimum_price + difference * 0.236
    second_level = minimum_price + difference * 0.382
    third_level = minimum_price + difference * 0.5
    forth_level = minimum_price + difference * 0.618 
    fifth_level = minimum_price + difference * 0.786 
    return {'y0.236':first_level, 'y0.382':second_level, 'y0.5':third_level, 'y0.618':forth_level,'y0.786':fifth_level}
