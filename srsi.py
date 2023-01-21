from analyzers import stoch_rsi
from get_data import get_data
import cufflinks as cf

ohlc = get_data()
srsi = stoch_rsi.StochasticRSI()
results = srsi.analyze(ohlc)

# cf.set_config_file(offline = True)
# results.iplot()