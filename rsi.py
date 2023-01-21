""" RSI Indicator
"""

from curses import pair_number
import math

import pandas
import pandas as pd
from talib import abstract

from .utils import IndicatorUtils



class RSI(IndicatorUtils):
    def analyze(self,historical_data, period_count=14,
                signal=['rsi'], hot_thresh=None, cold_thresh=None,  lrsi_filter=None):
        """Performs an RSI analysis on the historical data

        Args:
            historical_data (list): A matrix of historical OHCLV data.
            period_count (int, optional): Defaults to 14. The number of data points to consider for
                our RSI.
            signal (list, optional): Defaults to rsi. The indicator line to check hot/cold
                against.
            hot_thresh (float, optional): Defaults to None. The threshold at which this might be
                good to purchase.
            cold_thresh (float, optional): Defaults to None. The threshold at which this might be
                good to sell.

        Returns:
            pandas.DataFrame: A dataframe containing the indicators and hot/cold values.
        """

        dataframe = historical_data
        rsi_values = pd.DataFrame(abstract.RSI(dataframe.Close, period_count))
        # rsi_values.dropna(how='all', inplace=True)
        rsi_values.rename(columns={rsi_values.columns[0]: 'rsi'}, inplace=True)

        return rsi_values
