from re import S
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from kucoin.client import Client
from datetime import datetime
import time
from tenacity import retry, retry_if_exception_type, stop_after_attempt
import ccxt



client = Client("628a2ce9f39c9b000139b5cf", "04e61232-4199-490f-b097-2453665abdbe", "Ms..556655@")
start = time.mktime(datetime.strptime("2022/07/01", "%Y/%m/%d").timetuple())
end = time.mktime(datetime.strptime("2022/05/31", "%Y/%m/%d").timetuple())

@retry(retry=retry_if_exception_type(ccxt.NetworkError),stop=stop_after_attempt(10))
def get_data(pair):
    
    candles = client.get_kline_data(symbol=pair,kline_type='4hour',start=int(start))

    ohlc = pd.DataFrame(candles)

    ohlc.rename(columns={0: 'date', 1: 'open',2:'close',3:'high',4:'low',5:'volume',6:'amount'}, inplace=True)
    print(pair+" is analysing ")


    ohlc['date'] = ohlc['date'].astype(int)

    for x in range(0 , ohlc.shape[0]):
      ohlc.date[x] = datetime.fromtimestamp(ohlc.date[x]).strftime('%Y-%m-%d %H:%M:%S')

    ohlc=ohlc.sort_values(by=["date"], ascending=True)
    ohlc=ohlc.set_index('date')
    ohlc=ohlc.astype(float)
    return ohlc

def get_data_without_date():
    candles = client.get_kline_data(symbol='BTC-USDT',kline_type='15min',start=int(start))


    ohlc = pd.DataFrame(candles)
    ohlc.rename(columns={0: 'date', 1: 'open',2:'close',3:'high',4:'low',5:'volume',6:'amount'}, inplace=True)



    ohlc['date'] = ohlc['date'].astype(int)
    ohlc['high'] = ohlc['high'].astype(float)
    ohlc['low'] = ohlc['low'].astype(float)
    ohlc['close'] = ohlc['close'].astype(float)
    ohlc['open'] = ohlc['open'].astype(float)
    for x in range(0 , ohlc.shape[0]):
      ohlc.date[x] = datetime.fromtimestamp(ohlc.date[x]).strftime('%Y-%m-%d %H:%M:%S')

    ohlc=ohlc.iloc[::-1]
    return ohlc
# cf.set_config_file(offline = True)

# qf = cf.QuantFig(ohlc)

#qf.add_trendline(ohlc.index[0], ohlc.index[ohlc.shape[0]-1], on='close', to_strfmt='%Y-%m-%d %H:%M:%S')
# qf.add_rsi(periods=14 , rsi_upper=70, rsi_lower=30)
# print(qf.add_ema(periods=20))
# qf.add_macd()
#qf.iplot(title="btc-usdt")

print(get_data('BTC-USDT'))