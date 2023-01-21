from analyzers import atr
from test import get_data

atrs = atr.ATR()


ohlc =get_data('BTC-USDT',timeframe='4h')
print(ohlc)
rsis= atrs.analyze(ohlc,period_count=14)
print(rsis)
