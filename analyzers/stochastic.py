""" MACD Indicator
"""

import math

import pandas
from talib import abstract




class STOCH():
    def analyze(historical_data):

        results = abstract.STOCH(historical_data,fastk_period=14,slowk_period=1,slowd_period=3)

        return results
