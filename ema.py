""" EMA Indicator
"""

import math

import pandas
from talib import abstract

from .utils import IndicatorUtils


class EMA(IndicatorUtils):
    def analyze(self, historical_data, period_count=15):
        """Performs an EMA analysis on the historical data

                Args:
                        historical_data (list): A matrix of historical OHCLV data.
                        period_count (int, optional): Defaults to 15. The number of data points to consider for
                                our exponential moving average.

                Returns:
                        pandas.DataFrame: A dataframe containing the indicators and hot/cold values.
                """

        ema_values = pandas.DataFrame(abstract.EMA(historical_data.Close, period_count))
        ema_values.dropna(how='all', inplace=True)
        ema_values.rename(columns={0: 'ema'}, inplace=True)

        return ema_values
