from analyzers import ema
from analyzers import macd
from test import get_data
from send_to_channel import send_mina,send_main
import time
from datetime import datetime
import pytz
import pandas as pd
from  sync_multi_timeframe import *
import sys
macd_func = macd.MACD()
ema_func = ema.EMA()

class bcolors:
    OK = '\033[92m' #GREEN
    DOWN = '\033[93m' #YELLOW
    UP = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
timeframe_main=str(sys.argv[1])
timeframe_macd ='30h'
tz_London = pytz.timezone('Europe/London')
now = datetime.now(tz_London)
current_time = now.strftime("%d/%m/%Y %H:%M:%S")

pairs=['BTC-USDT','ETH-USDT','ADA-USDT','AXS-USDT','SOL-USDT','IOST-USDT','FLOW-USDT','IOTX-USDT','XMR-USDT','ETC-USDT','XTZ-USDT'
        ,'EGLD-USDT','SAND-USDT','BNB-USDT','ADA-USDT','XRP-USDT','CAKE-USDT','DOGE-USDT','DOT-USDT','AVAX-USDT','MATIC-USDT'
        ,'ALGO-USDT','ICP-USDT','VET-USDT','AAVE-USDT','AXS-USDT','UNI-USDT','FIL-USDT','SHIB-USDT','EOS-USDT','KCS-USDT'
        ,'NEAR-USDT','LTC-USDT','ATOM-USDT','LINK-USDT','BCH-USDT','TRX-USDT','XLM-USDT','MANA-USDT','HBAR-USDT','APE-USDT','FTM-USDT','GRT-USDT'
        ,'THETA-USDT','MKR-USDT']


for pair in pairs:
    if(timeframe_main =='4h'):
        timeframe_macd = '1h'
    elif(timeframe_main == '1h'):
        timeframe_macd = '30m'
    elif(timeframe_main == '30m'):
        timeframe_macd = '15m'
    elif(timeframe_main == '15m'):
        timeframe_macd = '5m'
    elif (timeframe_main == '5m'):
        timeframe_macd = '1m'

    ohlc_main = get_data(pair,timeframe_main,limit=200)
    ohlc_macd = get_data(pair,timeframe_macd,limit=200)
    macds = macd_func.analyze(ohlc_macd)
    emas = ema_func.analyze(ohlc_main,100)


    #macd calculation an syncronization
    if(timeframe_main=='4h'):
        macds = sync_4h_to_1h(ohlc_main, macds)
    elif (timeframe_main == '1h'):
        macds = sync_1h_to_30m(ohlc_main, macds)
    elif (timeframe_main == '30m'):
        macds = sync_30m_to_15m(ohlc_main, macds)
    elif (timeframe_main == '15m'):
        macds = sync_15m_to_5m(ohlc_main, macds)
    elif (timeframe_main == '5m'):
        macds = sync_5m_to_1m(ohlc_main, macds)

    macds = pd.merge(macds, ohlc_main, left_index=True, right_index=True)
    print(macds.tail(10))



    ema_count = emas.shape[0]
    macd_count = macds.shape[0]




    macd1 = macds.macd[macd_count-1]
    macd2 = macds.macd[macd_count-2]
    macd3 = macds.macd[macd_count-3]

    signal1 = macds.macdsignal[macd_count-1]
    signal2 = macds.macdsignal[macd_count-2]
    signal3 = macds.macdsignal[macd_count-3]




    ema1 = emas.ema[ema_count-1]
    ema2 = emas.ema[ema_count-2]
    ema3 = emas.ema[ema_count-3]

    ohlc_main_count = ohlc_main.shape[0]

    ohlc_main1 = ohlc_main.close[ohlc_main_count-1]
    ohlc_main2 = ohlc_main.close[ohlc_main_count-2]
    ohlc_main3 = ohlc_main.close[ohlc_main_count-3]
    print(f"ema1: {ema1} and ema2: {ema2}")
    print(f"macd1: {macd1} and macd2: {macd2}")
    print(f"signal1: {signal1} and signal2: {signal2}")
    print(f"close1: {ohlc_main1} and close2: {ohlc_main2}")

    if ohlc_main1 > ohlc_main2 and ohlc_main1 > ema1 and ohlc_main2 < ema2:
        if signal1 < macd1 and signal2 > macd2:
            print(bcolors.UP+"up signal signal with ema and macd strategy"+bcolors.RESET)
            print(bcolors.UP+"price is: "+str(ohlc_main1)+bcolors.RESET)
            message = pair+"\n"+"TIME:"+current_time+"\n"+"time frame: "+str(timeframe_main)+"\n"+"BUY signal with ema and macd strategy"+"\n"+"price is: "+str(ohlc_main1)+"\n"
            # send_mina(message)
            # send_main(message)
            print(message)
    elif ohlc_main1 < ohlc_main2 and ohlc_main1 < ema1 and ohlc_main2 > ema2:
        if signal1 > macd1 and signal2 < macd2:
            print(bcolors.DOWN+"down signal with ema and macd strategy"+bcolors.RESET)
            print(bcolors.DOWN+"price is: "+str(ohlc_main1)+bcolors.RESET)
            message = pair+"\n"+"TIME:"+current_time+"\n"+"time frame: "+str(timeframe_main)+"\n"+"SELL signal with ema and macd strategy"+"\n"+"price is: "+str(ohlc_main1)+"\n"
            # send_mina(message)
            # send_main(message)
            print(message)

