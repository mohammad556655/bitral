import ccxt
from re import S
import pandas as pd
import numpy
import calendar
from tenacity import retry, retry_if_exception_type, stop_after_attempt

import matplotlib.pyplot as plt
from datetime import datetime
import time

exchange_id = 'kraken'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({

    
})

start = time.mktime(datetime.strptime("2022/03/01", "%Y/%m/%d").timetuple())
end = time.mktime(datetime.strptime("2022/05/31", "%Y/%m/%d").timetuple())

now = datetime.utcnow()
unixtime = calendar.timegm(now.utctimetuple())

since = (start) * 1000 

@retry(retry=retry_if_exception_type(ccxt.NetworkError),stop=stop_after_attempt(10))

def get_data(pair,timeframe='1h', limit=500):
    print(pair+" is analysing ")
    if exchange.has['fetchOHLCV']:
        candles = exchange.fetch_ohlcv(symbol = pair, timeframe = timeframe, limit = limit)    

    ohlc = pd.DataFrame(candles,columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    ohlc['Date'] = [datetime.fromtimestamp(float(time)/1000) for time in ohlc['Date']]
    ohlc.set_index('Date', inplace=True)
    return ohlc