""" MACD Indicator
"""

import math

import pandas
from talib import abstract

from .utils import IndicatorUtils


class MACD(IndicatorUtils):
    def analyze(self, historical_data,fastperiod=12, slowperiod=26, signalperiod=9):
        """Performs a macd analysis on the historical data

        Args:
            historical_data (list): A matrix of historical OHCLV data.

        Returns:
            pandas.DataFrame: A dataframe containing the indicators and hot/cold values.
        """

        macd_values = abstract.MACD(historical_data,fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod).iloc[:]
        macd_values.dropna(how='all', inplace=True)

        return macd_values
