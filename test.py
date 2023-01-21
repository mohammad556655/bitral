import ccxt

import pandas as pd
import numpy
import calendar
from tenacity import retry, retry_if_exception_type, stop_after_attempt

import matplotlib.pyplot as plt
#from pandas_datareader import data
from kucoin.client import Client
# import cufflinks as cf
from datetime import datetime
import time

exchange_id = 'kucoin'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': "628a2ce9f39c9b000139b5cf",
    'secret': "04e61232-4199-490f-b097-2453665abdbe",
    'api_passphrase': "Ms..556655@",
    
    'enableRateLimit': True

    
})
exchange.options['adjustForTimeDifference'] = False
client = Client("628a2ce9f39c9b000139b5cf", "04e61232-4199-490f-b097-2453665abdbe", "Ms..556655@")
start = time.mktime(datetime.strptime("2022/05/01", "%Y/%m/%d").timetuple())
end = time.mktime(datetime.strptime("2022/05/31", "%Y/%m/%d").timetuple())

now = datetime.utcnow()
unixtime = calendar.timegm(now.utctimetuple())

since = (start- 60*60) * 1000 

@retry(retry=retry_if_exception_type(ccxt.NetworkError),stop=stop_after_attempt(10))
def get_data(pair,timeframe='1h',limit=2000,since=None):
    
    
    
    print(pair+" is analysing ")
    if exchange.has['fetchOHLCV']:
        if since ==None :
            candles = exchange.fetch_ohlcv(symbol=pair, timeframe=timeframe,limit=limit)
        else:
            startDate = since
            startDate = datetime.strptime(startDate, "%Y-%m-%d")
            startDate = datetime.timestamp(startDate)
            startDate = int(startDate) * 1000
            candles = exchange.fetch_ohlcv(symbol=pair, timeframe=timeframe,since=startDate)
    
    ohlc = pd.DataFrame(candles,columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    ohlc['Date'] = [datetime.fromtimestamp(float(time)/1000) for time in ohlc['Date']]
    # print(ohlc)
    ohlc.set_index('Date', inplace=True)
    return ohlc

def get_data_without_date():
    candles = client.get_kline_data(symbol='BTC-USDT',kline_type='4hour',start=int(start))


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
# pairs=['BTC-USDT','ETH-USDT','ADA-USDT','AXS-USDT','SOL-USDT','IOST-USDT','FLOW-USDT','IOTX-USDT','XMR-USDT','ETC-USDT','XTZ-USDT'
#         ,'EGLD-USDT','SAND-USDT','BNB-USDT','ADA-USDT','XRP-USDT','CAKE-USDT','DOGE-USDT','DOT-USDT','AVAX-USDT','MATIC-USDT'
#         ,'ALGO-USDT','ICP-USDT','VET-USDT','AAVE-USDT','AXS-USDT','UNI-USDT','FIL-USDT','SHIB-USDT','EOS-USDT','KCS-USDT'
#         ,'NEAR-USDT','LTC-USDT','ATOM-USDT','LINK-USDT','BCH-USDT','TRX-USDT','XLM-USDT','MANA-USDT','HBAR-USDT','APE-USDT','FTM-USDT','GRT-USDT'
#         ,'THETA-USDT','MKR-USDT']

# for pair in pairs:

#     ohlc= get_data(pair)
#     print(ohlc)
# cf.set_config_file(offline = True)

# qf = cf.QuantFig(ohlc)

#qf.add_trendline(ohlc.index[0], ohlc.index[ohlc.shape[0]-1], on='close', to_strfmt='%Y-%m-%d %H:%M:%S')
# qf.add_rsi(periods=14 , rsi_upper=70, rsi_lower=30)
# print(qf.add_ema(periods=20))
# qf.add_macd()
#qf.iplot(title="btc-usdt")

