from analyzers import dtoscillator
from get_data import get_data
import cufflinks as cf

ohlc = get_data('BTC-USDT')
srsi = dtoscillator.StochasticRSI()
results = srsi.analyze(ohlc,8)
print(results)
# cf.set_config_file(offline = True)
# results.iplot()