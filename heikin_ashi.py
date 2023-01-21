import pandas as pd

def make_heikin(ohlc):

    colomns = ['Open', 'High', 'Low', 'Close']
    HAdf = pd.DataFrame(columns=colomns)
    HAdf.Close= ((ohlc.Open + ohlc.High + ohlc.Low+ ohlc.Close)/4)

    for i in range(0,ohlc.shape[0]):
        if i == 0:
            HAdf.iat[0,0] = ((ohlc.Open.iloc[0] + ohlc.Close.iloc[0])/2)
        else:
            HAdf.iat[i,0] = ((HAdf.iat[i-1,0] + HAdf.iat[i-1,3])/2)
    HAdf.High = HAdf.loc[:,['Open', 'Close']].join(ohlc.High).max(axis=1)
    HAdf.Low = HAdf.loc[:,['Open', 'Close']].join(ohlc.Low).min(axis=1)
    
    return HAdf


    