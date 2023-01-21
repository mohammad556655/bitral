""" Stochastic RSI Indicator
"""

import math

import numpy as np
import pandas
from typing import Union
from talib import abstract

from .utils import IndicatorUtils


def willr(candles, period=14):
    """
    WILLR - Williams' %R

    :param candles: np.ndarray
    :param period: int - default=14


    :return: float | np.ndarray
    """

    res = abstract.WILLR(candles, timeperiod=period).to_frame()
    res.rename(columns={res.columns[0]: 'willr'}, inplace=True)
    return res