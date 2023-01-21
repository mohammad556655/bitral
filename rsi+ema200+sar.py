from cgitb import reset
from unittest import result
from analyzers import rsi
from analyzers import ema
from test import get_data
from analyzers import sar
import heikin_ashi
from send_to_channel import send_mina,send_main
import fibo_retrace
import time
from datetime import datetime
import pytz



class bcolors:
    OK = '\033[92m' #GREEN
    DOWN = '\033[93m' #YELLOW
    UP = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
timeframe='1h'
tz_London = pytz.timezone('Europe/London')
now = datetime.now(tz_London)
current_time = now.strftime("%d/%m/%Y %H:%M:%S")
rsi = rsi.RSI()
ema = ema.EMA()
sar = sar.SAR()
pairs=['BTC-USDT','ETH-USDT','ADA-USDT','AXS-USDT','SOL-USDT','IOST-USDT','FLOW-USDT','IOTX-USDT','XMR-USDT','ETC-USDT','XTZ-USDT'
        ,'EGLD-USDT','SAND-USDT','BNB-USDT','ADA-USDT','XRP-USDT','CAKE-USDT','DOGE-USDT','DOT-USDT','AVAX-USDT','MATIC-USDT'
        ,'ALGO-USDT','ICP-USDT','VET-USDT','AAVE-USDT','AXS-USDT','UNI-USDT','FIL-USDT','SHIB-USDT','EOS-USDT','KCS-USDT'
        ,'NEAR-USDT','LTC-USDT','ATOM-USDT','LINK-USDT','BCH-USDT','TRX-USDT','XLM-USDT','MANA-USDT','HBAR-USDT','APE-USDT','FTM-USDT','GRT-USDT'
        ,'THETA-USDT','MKR-USDT']
for pair in pairs:
    ohlc = get_data(pair,timeframe,limit=500)
    heikin = heikin_ashi.make_heikin(ohlc=ohlc)
    # print(ohlc)
    # adxs = adx.analyze(ohlc,14)
    rsis = rsi.analyze(heikin,14)
    emas = ema.analyze(heikin,100)
    sars = sar.analyze(heikin.High,heikin.Low)



    sar_count = sars.shape[0]-1
    rsi_count = rsis.shape[0]-1
    ema_count = emas.shape[0]-1
    ohlc_count = heikin.shape[0]-1
    close1 = heikin.Close[ohlc_count]
    close2 = heikin.Close[ohlc_count-1]
    close3 = heikin.Close[ohlc_count-2]

    open1 = heikin.Open[ohlc_count]
    open2 = heikin.Open[ohlc_count - 1]
    open3 = heikin.Open[ohlc_count - 2]

    low1 = heikin.Low[ohlc_count]
    low2 = heikin.Low[ohlc_count - 1]
    low3 = heikin.Low[ohlc_count - 2]

    high1 = heikin.High[ohlc_count]
    high2 = heikin.High[ohlc_count - 1]
    high3 = heikin.High[ohlc_count - 2]

    rsi1 = rsis.rsi[rsi_count]
    rsi2 = rsis.rsi[rsi_count-1]
    rsi3 = rsis.rsi[rsi_count-2]

    ema1 = emas.ema[ema_count]
    ema2= emas.ema[ema_count-1]
    ema3 = emas.ema[ema_count-2]

    sar1 = sars.sar[sar_count]
    sar2 = sars.sar[sar_count-1]
    sar3 = sars.sar[sar_count-2]
    # print(heikin)
    # print(sars)
    # print(rsis)
    message=""
    ema_for_up = ema1 + (ema1*0.005)
    ema_for_down = ema1 - (ema1*0.005)
    # 1th candle
# قیمت از زیر ema 100 بره بالای 100 و هزمان پارابولیک زیر قیمت باشه و rsi بالای 50 باشه

    if rsi1>rsi2 and rsi1>50 and rsi1<70:
        if ema_for_up <= close1 :
            if sar1 < low1 and sar2 > high2:
                print(bcolors.UP + "up signal signal with sar strategy" + bcolors.RESET)
                print(bcolors.UP + "price is: " + str(close1) + bcolors.RESET)
                sl= sar1
                fib_result = fibo_retrace.find_fib_up(ohlc.tail(50),min=ohlc.Low[ohlc_count])
                target1 = fib_result['y0.5']
                target2 = fib_result['y0.382']
                print(message)
                message = pair + "\n" + "TIME:" + current_time + "\n" + "time frame: " + str(timeframe) + "\n" + "BUY signal with sar strategy" + "\n" + "price is: " + str(close1) + "\n"+"Stop Loss= " +str(sl) + "\n"+"Target1= " +str(target1)+ "\n"+"Target2= " +str(target2)
                print(message)
                send_mina(message)
                # send_main(message)
                print(message)
                print(f"rsi1= {rsi1} and rsi2= {rsi2}")


    elif rsi1<rsi2 and rsi1>30 and rsi1<50 :
        if ema_for_down >= close1:
            if sar1 >high1 and sar2 <low2:
                print(bcolors.DOWN + "down signal with sar strategy" + bcolors.RESET)
                print(bcolors.DOWN + "price is: " + str(close1) + bcolors.RESET)
                sl = sar1
                fib_result = fibo_retrace.find_fib_down(ohlc.tail(50),min=ohlc.High[ohlc_count])
                target1 = fib_result['y0.5']
                target2 = fib_result['y0.382']
                message = pair + "\n" + "TIME:" + current_time + "\n" + "time frame: " + str(timeframe) + "\n" + "SELL signal with sar strategy" + "\n" + "price is: " + str(close1) + "\n"+"Stop Loss= " +str(sl) + "\n"+"Target1= " +str(target1)+ "\n"+"Target2= " +str(target2)
                print(message)
                send_mina(message)
                # send_main(message)
                print(message)
                print(f"rsi1= {rsi1} and rsi2= {rsi2}")

    message=""