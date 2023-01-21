import numpy as np
from datetime import datetime

from backtesting import Backtest, Strategy
from backtesting.test import EURUSD, GOOG
import numpy as np
from backtesting.lib import crossover
import talib
import pandas_ta as ta
import pandas as pd
from test import get_data
x = pd.read_csv(".\ohlc_data\Kucoin_BTCUSDT_1h.csv")
# x = get_data("BTC-USDT",timeframe='1h',since="2020-05-19")
print(x)
print(GOOG.dtypes)
GOOG = x
class RsiOscillator(Strategy):

    cmo_upper = 50
    cmo_lower = -50
    rsi_upper = 70
    rsi_lower = 30
    rsi_window = 14
    cmo_window = 20
    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)
        self.ema = self.I(talib.EMA, self.data.Close, 100)
        self.sar = self.I(talib.SAR, self.data.High,self.data.Low)
        self.cmo = self.I(ta.cmo, pd.Series(self.data.Close),self.cmo_window, talib= False)

    def next(self):
        price = self.data.Close[-1]
        tp_sell =  (1.5*price) - price
        if self.ema[-1] < price and self.sar[-1]<price and self.sar[-2]> self.data.Close[-2] and self.rsi[-1]>50 and self.rsi[-1]<70 :
            self.buy()

        if self.ema[-1] > price and self.sar[-1] > price and self.sar[-2] < self.data.Close[-2] and self.rsi[-1] < 50 and self.rsi[-1]>30:
            self.sell()
        if self.position.is_long and self.sar[-1]> self.data.Close:
            self.position.close()
        if self.position.is_short and self.sar[-1] < self.data.Close:
            self.position.close()

bt = Backtest(GOOG,RsiOscillator,cash = 10_0000000)
state = bt.run()
# state = bt.optimize(
#     rsi_window = range(1,50,1),
#     maximize='Sharpe Ratio'
# )

print(state)
bt.plot()