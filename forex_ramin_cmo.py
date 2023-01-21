from cgitb import reset
import sys
from unittest import result
from analyzers import cmo
from analyzers import rsi
from analyzers import ema
import negative_divergant
import positive_divergent
import time
from datetime import datetime
from analyzers import atr
from forex_getdata import get_data
from send_to_channel import send_ramin,send_main
import pytz
import fibo_retrace
rsi = rsi.RSI()
cmo = cmo.CMO()
atr = atr.ATR()
tz_London = pytz.timezone('Europe/London')
now = datetime.now(tz_London)
current_time = now.strftime("%d/%m/%Y %H:%M:%S")
class bcolors:
    OK = '\033[92m' #GREEN
    DOWN = '\033[93m' #YELLOW
    UP = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


timeframe = str(sys.argv[1])
pairs=["EURUSD=X","AUDUSD=X","USDJPY=X","GBPUSD=X","USDCAD=X","USDCNY=X","USDCHF=X","USDHKD=X","USDKRW=X","EURGBP=X"]
# pairs=['BTC-USDT','ETH-USDT']
for pair in pairs:
    ohlc = get_data(pair,timeframe=timeframe,period='1mo')
    print(ohlc)

    rsis = rsi.analyze(ohlc,14)
    cmos = cmo.analyze(ohlc,period_count=20)
    atrs = atr.analyze(ohlc,period_count=14)
    print(cmos)
    print(rsis)
    print(atrs)
    rsi_count = rsis.shape[0] - 1
    cmo_count = cmos.shape[0] - 1
    ohlc_count = ohlc.shape[0] - 1
    atr_count = atrs.shape[0] - 1

    cmo1 = cmos.cmo[cmo_count]
    cmo2 = cmos.cmo[cmo_count-1]
    cmo3 = cmos.cmo[cmo_count-2]

    rsi1 = rsis.rsi[rsi_count]
    rsi2 = rsis.rsi[rsi_count-1]
    rsi3 = rsis.rsi[rsi_count-2]
    Close1 = ohlc.Close[ohlc_count]

    atr1 = atrs.atr[atr_count]
    atr2 = atrs.atr[atr_count-1]
    atr3 = atrs.atr[atr_count-2]
    # print(ohlc)
    # print(ohlc_50)
    # positive_div_result = positive_divergent.find_pos_rsi_div(pair, timeframe=timeframe,ohlc = ohlc_50)
    # print(positive_div_result)
    message=""
    
    rsi_20 = rsis.tail(20)
    print(rsi1)
    print(cmo1)
    print(cmo2)
    cmo_20 = cmos.tail(20)
    ohlc_50 = ohlc.tail(50)
    rsi_20 = rsi_20.reset_index()
    # print(cmo_20)
    # print(atr1)
    if rsi1<29  and cmo1<-50 and cmo2>-50 :
            positive_div_result = positive_divergent.find_pos_rsi_div(pair, timeframe=timeframe,ohlc = ohlc_50)
            if positive_div_result.shape[0]>0:
                positive_div_result = positive_div_result.sort_values('date2',ascending=True)
                # if (ohlc_50.index[-1]==positive_div_result.date2.iloc[-1]):
                print(positive_div_result)
                stop_loss = Close1 - (atr1*1.8)
                fib_result = fibo_retrace.find_fib_up(ohlc.tail(400),max=ohlc.High[ohlc_count])
                target1 = fib_result['y0.5']
                target2 = fib_result['y0.382']
                print(bcolors.UP + "up signal signal with cmo strategy" + bcolors.RESET)
                print(bcolors.UP + "price is: " + str(Close1) + bcolors.RESET)
                message = message + pair + "\n" + "time frame: " + str(timeframe) + "\n" + "BUY signal for ramin" + "\n" + "price is: " + str(Close1) + "\n"+"Stop Loss= " +str(stop_loss) + "\n"+"Target1= " +str(target1)+ "\n"+"Target2= " +str(target2)
                print(message)
                # print(ohlc_50.index[-1])
                print(f"rsi1= {rsi1} cmo1= {cmo1} and cmo2= {cmo2}\n \n")
                send_ramin(message)
                    # send_main(message)

    elif rsi1>71 and cmo1>50 and cmo2<50 :
        # for i in range (1 ,cmo_20.shape[0]):
            negative_div_result = negative_divergant.find_neg_rsi_div(pair, timeframe=timeframe,ohlc = ohlc_50)
            if(negative_div_result.shape[0]>0):
                negative_div_result = negative_div_result.sort_values('date2',ascending=True)
                # if (ohlc_50.index[-1]==negative_div_result.date2.iloc[-1]):
                print(negative_div_result)
                stop_loss = Close1 + (atr1*1.8)
                fib_result = fibo_retrace.find_fib_down(ohlc.tail(400),min=ohlc.Low[ohlc_count])
                target1 = fib_result['y0.5']
                target2 = fib_result['y0.382']
                print(bcolors.DOWN + "down signal with cmo strategy" + bcolors.RESET)
                print(bcolors.DOWN + "price is: " + str(Close1) + bcolors.RESET)
                message = message + pair + "\n" + "time frame: " + str(timeframe) + "\n" + "SELL signal for ramin" + "\n" + "price is: " + str(Close1) + "\n"+"Stop Loss= " +str(stop_loss) + "\n"+"Target1= " +str(target1)+ "\n"+"Target2= " +str(target2)
                print(message)
                # print(ohlc_50.index[-1])
                print(f"rsi1= {rsi1} cmo1= {cmo1} and cmo2= {cmo2}\n \n")
                send_ramin(message)
                # send_main(message)

