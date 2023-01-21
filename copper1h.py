from curses import KEY_A1
from analyzers import bollinger
from operator import truediv
from analyzers import willr
from analyzers import rsi
from analyzers import ichimoku
from analyzers import stochastic
from test import get_data
from send_to_channel import send
import time
from analyzers import adx
from analyzers import keltner
from analyzers import Coppock_Curve as cp
from datetime import datetime
import pytz


import cufflinks as cf
pairs=['BTC-USDT','ETH-USDT','ADA-USDT','AXS-USDT','SOL-USDT','IOST-USDT','FLOW-USDT','XMR-USDT','ETC-USDT','XTZ-USDT'
        ,'EGLD-USDT','SAND-USDT','ADA-USDT','XRP-USDT','CAKE-USDT','DOGE-USDT','DOT-USDT','AVAX-USDT','MATIC-USDT'
        ,'ALGO-USDT','ICP-USDT','VET-USDT','AAVE-USDT','AXS-USDT','UNI-USDT','FIL-USDT','SHIB-USDT','EOS-USDT','KCS-USDT'
        ,'LTC-USDT','ATOM-USDT','LINK-USDT','BCH-USDT','TRX-USDT','XLM-USDT','MANA-USDT','HBAR-USDT','APE-USDT','FTM-USDT','GRT-USDT'
        ,'THETA-USDT','MKR-USDT','DYP-USDT']
class bcolors:
    OK = '\033[92m' #GREEN
    DOWN = '\033[93m' #YELLOW
    UP = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR 
timeframe='1h' 
tz_London = pytz.timezone('Europe/London')
now = datetime.now(tz_London)

current_time = now.strftime("%d/%m/%Y %H:%M:%S")

for pair in pairs:
    adxs = adx.Adx()

    ohlc =get_data(pair,timeframe)


    ohlc_count = ohlc.shape[0]-1
    close1 = ohlc.close[ohlc_count]
    close2 = ohlc.close[ohlc_count-1]
    close3 = ohlc.close[ohlc_count-2]
    close4 = ohlc.close[ohlc_count-3]
    close5 = ohlc.close[ohlc_count-4]
    

    cc = cp.get_cc(ohlc.close, 14, 11, 10)
    i = cc.shape[0]-1
    message=""

    # 1th candle
    if(cc[i-4] < 0 and cc[i-3] < 0 and cc[i-2] < 0 and cc[i-1] < 0 and cc[i] > 0):
        print(bcolors.UP+"up signal signal with copper curve strategy"+bcolors.RESET)
        print(bcolors.UP+"price is: "+str(close1)+bcolors.RESET)
        message = pair+"\n"+"TIME:"+current_time+"\n"+"time frame: "+str(timeframe)+"\n"+"BUY signal with copper curve strategy"+"\n"+"price is: "+str(close1)
        send(message)


    elif cc[i-4] > 0 and cc[i-3] > 0 and cc[i-2] > 0 and cc[i-1] > 0 and cc[i] < 0:
        print(bcolors.DOWN+"down signal with copper curve strategy"+bcolors.RESET)
        print(bcolors.DOWN+"price is: "+str(close1)+bcolors.RESET)
        message = pair+"\n"+"TIME:"+current_time+"\n"+"time frame: "+str(timeframe)+"\n"+"SELL signal with copper curve strategy"+"\n"+"price is: "+str(close1)
        send(message)


    message=""



