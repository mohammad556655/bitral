import numpy as np
def wma(data, lookback):
    weights = np.arange(1, lookback + 1)
    val = data.rolling(lookback)
    wma = val.apply(lambda prices: np.dot(prices, weights) / weights.sum(), raw = True)
    return wma

def get_roc(close, n):
    difference = close.diff(n)
    nprev_values = close.shift(n)
    roc = (difference / nprev_values) * 100
    return roc

def get_cc(data, roc1_n, roc2_n, wma_lookback):
    longROC = get_roc(data, roc1_n)
    shortROC = get_roc(data, roc2_n)
    ROC = longROC + shortROC
    cc = wma(ROC, wma_lookback).dropna()
    return cc

# aapl['cc'] = get_cc(aapl['close'], 14, 11, 10)
