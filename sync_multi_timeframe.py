import pandas as pd

def sync_4h_to_1h(ohlc,indicator):
    #shift 3
    len = indicator.shape[0]

    for i in range(0 , len):
        if(i+3<=len-1):
            indicator.macd[i] = indicator.macd[i+3]
            indicator.macdsignal[i] = indicator.macdsignal[i+3]
    return indicator

def sync_1h_to_30m(ohlc,indicator):
    #shift 1
    len = indicator.shape[0]

    for i in range(0 , len):
        if(i+1<=len-1):
            indicator.macd[i] = indicator.macd[i+1]
            indicator.macdsignal[i] = indicator.macdsignal[i+1]
    return indicator

def sync_30m_to_15m(ohlc,indicator):
    #shift 1
    len = indicator.shape[0]
    for i in range(0 , len):
        if(i+1<=len-1):
            indicator.macd[i] = indicator.macd[i+1]
            indicator.macdsignal[i] = indicator.macdsignal[i+1]
    return indicator

def sync_15m_to_5m(ohlc,indicator):
    #shift 2
    len = indicator.shape[0]
    for i in range(0 , len):
        if(i+2<=len-1):
            indicator.macd[i] = indicator.macd[i+2]
            indicator.macdsignal[i] = indicator.macdsignal[i+2]
    return indicator

def sync_5m_to_1m(ohlc,indicator):
    #shift 4
    len = indicator.shape[0]
    for i in range(0 , len):
        if(i+4<=len-1):
            indicator.macd[i] = indicator.macd[i+4]
            indicator.macdsignal[i] = indicator.macdsignal[i+4]
    return indicator