from cgitb import reset
from unittest import result
from analyzers import adx
from analyzers import rsi
from analyzers import ema
from kraken_getdata import get_data

import time
import calendar
from datetime import datetime

adx = adx.Adx()

ema = ema.EMA()
class bcolors:
    OK = '\033[92m' #GREEN
    DOWN = '\033[93m' #YELLOW
    UP = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


pairs=['EUR/CAD','EUR/CHF','USD/CHF','USD/JPY','GBP/USD','EUR/USD','USD/CAD','EUR/GBP','EUR/JPY']
    
for pair in pairs:
    ohlc = get_data(pair)
    print(ohlc)
    # rsis = rsi.RSI.analyze(ohlc,14)
    # adxs = adx.analyze(ohlc,14)
    # emas = ema.analyze(ohlc,50)

    # dmi_count = adxs.shape[0]-1
    # rsi_count = rsis.shape[0]-1
    # ema_count = emas.shape[0]-1
    # ohlc_count = ohlc.shape[0]-1
    
    # close = ohlc.close[ohlc_count]
    # try:
    #     rsi1 = rsis.rsi[rsi_count]
    #     rsi2= rsis.rsi[rsi_count-1]
    #     rsi3 = rsis.rsi[rsi_count-2] 
    # except KeyError:
    #     print("RSI values not found: KeyError....")


    # try:
    #     ema1 = emas.ema[ema_count]
    #     ema2 = emas.ema[ema_count-1]
    # except KeyError:
    #     print("EMA values not found: KeyError....")
    # try:
    #     pdi1 = adxs.pdi[dmi_count]
    #     ndi1= adxs.ndi[dmi_count]
    #     adx1 = adxs.adx[dmi_count]

    #     pdi2 = adxs.pdi[dmi_count-1]
    #     ndi2 = adxs.ndi[dmi_count-1]
    #     adx2 = adxs.adx[dmi_count-1]

    #     pdi3 = adxs.pdi[dmi_count-2]
    #     ndi3 = adxs.ndi[dmi_count-2]
    #     adx3 = adxs.adx[dmi_count-2]
    # except KeyError:
    #     print("DMI values not found: KeyError....")
    # if(close > ema1):
    #     if(rsi1>50 and rsi2>50):
    #         if(ndi1 < pdi1 and ndi2 < pdi2):
    #             if(adx1>=20 and adx1<= 25 and adx1>adx2):
    #                 print(bcolors.UP+"up adx signal"+bcolors.RESET)
    # elif(close < ema1):
    #     if(rsi1 < 50 and rsi2 < 50):
    #         if(ndi1 > pdi1 and ndi2 > pdi2):
    #             if(adx1>=20 and adx1<= 25 and adx1>adx2):
    #                 print(bcolors.DOWN+"down adx signal"+bcolors.RESET)
