""" ATR Indicator
"""

from curses import pair_number
import math

import pandas 
from talib import abstract




class ATR():
    def analyze(self,historical_data, period_count=14):


        dataframe = historical_data
        rsi_values = pandas.DataFrame(abstract.ATR(dataframe.High,dataframe.Low,dataframe.Close, period_count))
        rsi_values.dropna(how='all', inplace=True)
        rsi_values.rename(columns={rsi_values.columns[0]: 'atr'}, inplace=True)

        return rsi_values
