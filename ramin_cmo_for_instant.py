from cgitb import reset
import sys
from unittest import result
from analyzers import cmo
from analyzers import rsi
from analyzers import ema
from test import get_data
import negative_divergant
import positive_divergent
import time
from datetime import datetime
from send_to_channel import send_ramin,send_main
import pytz
rsi = rsi.RSI()
cmo = cmo.CMO()
tz_London = pytz.timezone('Europe/London')
now = datetime.now(tz_London)
current_time = now.strftime("%d/%m/%Y %H:%M:%S")
class bcolors:
    OK = '\033[92m' #GREEN
    DOWN = '\033[93m' #YELLOW
    UP = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


def analyze(ohlc,timeframe):
    ohlc_50 = ohlc.tail(50)
    rsis = rsi.analyze(ohlc,14)
    cmos = cmo.analyze(ohlc,period_count=20)
    # print(cmos)
    # print(rsis)
    rsi_count = rsis.shape[0] - 1
    cmo_count = cmos.shape[0] - 1
    ohlc_count = ohlc.shape[0] - 1
    cmo1 = cmos.cmo[cmo_count]
    cmo2 = cmos.cmo[cmo_count-1]
    cmo3 = cmos.cmo[cmo_count-2]

    rsi1 = rsis.rsi[rsi_count]
    rsi2 = rsis.rsi[rsi_count-1]
    rsi3 = rsis.rsi[rsi_count-2]
    close1 = ohlc.close[ohlc_count]


    message=""
    print(f"rsi1= {rsi1} and rsi2= {rsi2} and cmo1= {cmo1} and cmo2= {cmo2}")
    if rsi1<29  and cmo1<-50 and cmo2>-50 :
        positive_div_result = positive_divergent.find_pos_rsi_div(pair, timeframe=timeframe,ohlc = ohlc_50)
        if positive_div_result.empty == False:
            print(bcolors.UP + 'div yes' + bcolors.RESET)
            message = "div yes  "+"\n"
            print(bcolors.UP + "up signal signal with cmo strategy" + bcolors.RESET)
            print(bcolors.UP + "price is: " + str(close1) + bcolors.RESET)
            message = message + pair + "\n" + "TIME:" + current_time + "\n" + "time frame: " + str(timeframe) + "\n" + "BUY signal for ramin" + "\n" + "price is: " + str(close1) + "\n"
            print(message)
            # send_ramin(message)
        # send_main(message)

    elif rsi1>71 and cmo1>50 and cmo2<50 :
        negative_div_result = negative_divergant.find_neg_rsi_div(pair, timeframe=timeframe, ohlc = ohlc_50)
        if negative_div_result.empty == False:
            print(bcolors.DOWN+'div yes'+ bcolors.RESET)
            message = "div yes  "+"\n"
            print(bcolors.DOWN + "down signal with cmo strategy" + bcolors.RESET)
            print(bcolors.DOWN + "price is: " + str(close1) + bcolors.RESET)
            message = message + pair + "\n" + "TIME:" + current_time + "\n" + "time frame: " + str(timeframe) + "\n" + "SELL signal for ramin" + "\n" + "price is: " + str(close1) + "\n"
            print(message)
            # send_ramin(message)
        # send_main(message)
