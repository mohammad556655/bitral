from hashlib import new
from analyzers import macd
from get_data import get_data
import cufflinks as cf

ohlc = get_data()
macd = macd.MACD()
results = macd.analyze(ohlc)

# cf.set_config_file(offline = True)
# results.iplot()