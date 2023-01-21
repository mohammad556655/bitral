from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from test import get_data
from backtesting.lib import crossover
import talib
import pandas_ta as ta
import pandas as pd
import negative_divergant
import positive_divergent
# x = pd.read_csv(".\ohlc_data\Kucoin_BTCUSDT_1h.csv")
x = get_data("BTC-USDT",timeframe='1h',since="2020-05-19")
GOOG = x
# print(GOOG)
class RsiOscillator(Strategy):

    cmo_upper = 50
    cmo_lower = -50
    rsi_upper = 70
    rsi_lower = 30
    rsi_window = 14
    cmo_window = 20
    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)
        self.cmo = self.I(ta.cmo, pd.Series(self.data.Close),self.cmo_window, talib= False)
        self.atr = self.I(talib.ATR,self.data.High, self.data.Low, self.data.Close, 14)
        self.p_dive = None
        self.x_50 = None
        self.n_div = None
        # print(self.n_div)
        # print(self.atr)
    def next(self):
        price = self.data.Close[-1]

        atr = self.atr[-1]
        sl_sell = price + (atr*1.8)
        sl_buy = price - (atr * 1.8)

        tp_sell = abs((atr * 1.8)*3 - price)
        tp_buy = (atr * 1.8)*3 + price

        # if crossover(self.cmo,self.cmo_upper) and crossover(self.rsi,self.rsi_upper):
            # self.x_50 = self.data.df[-50:]

            # self.n_div = negative_divergant.find_neg_rsi_div('BTC-USDT', timeframe='1h', ohlc=self.x_50)
            # if self.n_div.shape[0]>0:
            # self.sell(tp=tp_sell, sl=sl_sell)


        if crossover(self.cmo_lower , self.cmo) and crossover(self.rsi_lower,self.rsi):
            self.x_50 = self.data.df[-50:]
            # print(self.x_50)
            # self.p_div = positive_divergent.find_pos_rsi_div('BTC-USDT', timeframe='1h', ohlc=self.x_50)

            # if self.p_div.shape[0]>0:
            self.buy(tp=tp_buy*1.5, sl=sl_buy)







        # if self.cmo[-1] > 50 and self.cmo[-2]<50 and self.rsi[-1]>70:
        #     self.sell(tp = 0.8*price , sl =1.1 *price)
        #
        # if self.cmo[-1]< -50 and self.cmo[-2]>-50 and self.rsi[-1]<30:
        #     self.buy(tp = 1.2 * price , sl = 0.90*price)

bt = Backtest(GOOG,RsiOscillator,cash = 10_000_0000)
state = bt.run()
# state = bt.optimize(
#     cmo_upper = range(0,100,2),
#     cmo_lower = (-100 , 0 ,2),
#
#     maximize='Sharpe Ratio'
# )

print(state)
bt.plot()