from cgitb import reset
from unittest import result
from analyzers import adx
from analyzers import rsi
from analyzers import ema
from test import get_data
from send_to_channel import send
from datetime import datetime
import time
import calendar
from datetime import datetime
from analyzers import mfi
import pytz

adx = adx.Adx()

ema = ema.EMA()
mfi = mfi.MFI()
class bcolors:
    OK = '\033[92m' #GREEN
    DOWN = '\033[93m' #YELLOW
    UP = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

timeframe='1h'
tz_London = pytz.timezone('Europe/London')
now = datetime.now(tz_London)

current_time = now.strftime("%d/%m/%Y %H:%M:%S")

pairs=['BTC-USDT','ETH-USDT','ADA-USDT','AXS-USDT','SOL-USDT','IOST-USDT','FLOW-USDT','IOTX-USDT','XMR-USDT','ETC-USDT','XTZ-USDT'
        ,'EGLD-USDT','SAND-USDT','BNB-USDT','ADA-USDT','XRP-USDT','CAKE-USDT','DOGE-USDT','DOT-USDT','AVAX-USDT','MATIC-USDT'
        ,'ALGO-USDT','ICP-USDT','VET-USDT','AAVE-USDT','AXS-USDT','UNI-USDT','FIL-USDT','SHIB-USDT','EOS-USDT','KCS-USDT'
        ,'NEAR-USDT','LTC-USDT','ATOM-USDT','LINK-USDT','BCH-USDT','TRX-USDT','XLM-USDT','MANA-USDT','HBAR-USDT','APE-USDT','FTM-USDT','GRT-USDT'
        ,'THETA-USDT','MKR-USDT','APE-USDT']
    
for pair in pairs:
    ohlc = get_data(pair,timeframe=timeframe)
    rsis = rsi.RSI.analyze(ohlc,14)
    adxs = adx.analyze(ohlc,14)
    emas = ema.analyze(ohlc,50)
    close1 = ohlc.close[-1]
    mfis = mfi.analyze(ohlc , period_count=14)
    dmi_count = adxs.shape[0]-1
    rsi_count = rsis.shape[0]-1
    ema_count = emas.shape[0]-1
    ohlc_count = ohlc.shape[0]-1
    mfi_count = mfis.shape[0]-1
    print(mfis)
    close = ohlc.close[ohlc_count]
    try:
        rsi1 = rsis.rsi[rsi_count]
        rsi2= rsis.rsi[rsi_count-1]
        rsi3 = rsis.rsi[rsi_count-2] 
    except KeyError:
        print("RSI values not found: KeyError....")


    try:
        ema1 = emas.ema[ema_count]
        ema2 = emas.ema[ema_count-1]
    except KeyError:
        print("EMA values not found: KeyError....")
    try:
        pdi1 = adxs.pdi[dmi_count]
        ndi1= adxs.ndi[dmi_count]
        adx1 = adxs.adx[dmi_count]

        pdi2 = adxs.pdi[dmi_count-1]
        ndi2 = adxs.ndi[dmi_count-1]
        adx2 = adxs.adx[dmi_count-1]

        pdi3 = adxs.pdi[dmi_count-2]
        ndi3 = adxs.ndi[dmi_count-2]
        adx3 = adxs.adx[dmi_count-2]
    except KeyError:
        print("DMI values not found: KeyError....")

    # print(adx1)
    # print(adx2)
    # print(adx3)
    # print(rsi1)
    # print(rsi2)
    # print(rsi3)
    # print(ema1)
    # print(ema2)
    message=''

    if(rsi1<50):
            if(ndi1 > pdi1):
                if(adx1>=35 and adx1<adx2 and adx2<adx3):
                    print(bcolors.UP+"up signal signal with DMI + RSI"+bcolors.RESET)
                    print(bcolors.UP+"price is: "+str(close1)+bcolors.RESET)
                    message = pair+"\n"+"TIME:"+current_time+"\n"+"time frame: "+str(timeframe)+"\n"+"BUY signal with DMI + RSI"+"\n"+"price is: "+str(close1)+"\n"+"adx is:"+str(adx1)
                    send(message)

    if(rsi1 > 50):
            if(ndi1 < pdi1):
                if(adx1>=35 and adx1<adx2 and adx2<adx3):
                    print(bcolors.DOWN+"down signal with DMI + RSI"+bcolors.RESET)
                    print(bcolors.DOWN+"price is: "+str(close1)+bcolors.RESET)
                    message = pair+"\n"+"TIME:"+current_time+"\n"+"time frame: "+str(timeframe)+"\n"+"SELL signal with DMI + RSI"+"\n"+"price is: "+str(close1)+"\n"+"adx is:"+str(adx1)
                    send(message)