from analyzers import willr
from get_data import get_data
import cufflinks as cf


ohlc =get_data('BTC-USDT')
rsis=willr.willr(ohlc,21)
print(rsis)

