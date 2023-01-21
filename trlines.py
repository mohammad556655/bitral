from analyzers import trendln
from test import get_data
import matplotlib.pyplot as plt
import cufflinks as cf
import pandas as pd

candles = get_data('XMR-USDT',timeframe='15m')
# trends = trendln.calc_support_resistance(candles.close,accuracy=8)
# ohlc = pd.DataFrame(trends)
# print(ohlc)
fig = trendln.plot_support_resistance(candles.close,accuracy=12)
# print(trendines)
# cf.set_config_file(offline = True)
plt.show()
# qf = cf.QuantFig(trendln)
# qf.iplot(title="btc-usdt")