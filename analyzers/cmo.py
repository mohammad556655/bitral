""" CMO Indicator
"""

from curses import pair_number
import math

import pandas 
from talib import abstract

from finta import TA
import pandas_ta as ta
class CMO():
    def analyze(self,historical_data, period_count=14):
        # """
        # CMO - Chande Momentum Oscillator

        # :param candles: np.ndarray
        # :param period: int - default=14
        # :param source_type: str - default: "close"
        # :param sequential: bool - default=False

        # :return: float | np.ndarray
        # """

        dataframe = historical_data
        # rsi_values = abstract.CMO(dataframe, period_count).to_frame()
        # rsi_values.dropna(how='all', inplace=True)
        # rsi_values.rename(columns={rsi_values.columns[0]: 'cmo'}, inplace=True)
        # rsi_values = TA.CMO(dataframe,period_count)
        cmo_values = ta.cmo(dataframe.Close,length=period_count,talib=False).to_frame()
        cmo_values.rename(columns={cmo_values.columns[0]: 'cmo'}, inplace=True)
        return cmo_values
