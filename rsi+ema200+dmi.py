from cgitb import reset
from unittest import result
from analyzers import adx
from analyzers import rsi
from analyzers import ema
from test import get_data
import time

adx = adx.Adx()
rsi = rsi.RSI()
ema = ema.EMA()
class bcolors:
    OK = '\033[92m' #GREEN
    DOWN = '\033[93m' #YELLOW
    UP = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


pairs=['BTC-USDT','ETH-USDT','ADA-USDT','AXS-USDT','SOL-USDT','IOST-USDT','FLOW-USDT','IOTX-USDT','XMR-USDT','ETC-USDT','XTZ-USDT'
        ,'EGLD-USDT','SAND-USDT','BNB-USDT','ADA-USDT','XRP-USDT','CAKE-USDT','DOGE-USDT','DOT-USDT','AVAX-USDT','MATIC-USDT'
        ,'ALGO-USDT','ICP-USDT','VET-USDT','AAVE-USDT','AXS-USDT','UNI-USDT','FIL-USDT','SHIB-USDT','EOS-USDT','KCS-USDT'
        ,'NEAR-USDT','LTC-USDT','ATOM-USDT','LINK-USDT','BCH-USDT','TRX-USDT','XLM-USDT','MANA-USDT','HBAR-USDT','APE-USDT','FTM-USDT','GRT-USDT'
        ,'THETA-USDT','MKR-USDT']
for pair in pairs:
    ohlc = get_data(pair)
    # print(ohlc)
    # adxs = adx.analyze(ohlc,14)
    # rsis = rsi.analyze(ohlc,14)
    # emas = ema.analyze(ohlc,200)

    # dmi_count = adxs.shape[0]-1
    # rsi_count = rsis.shape[0]-1
    # ema_count = emas.shape[0]-1
    # ohlc_count = ohlc.shape[0]-1
    
    # pdi1 = adxs.pdi[dmi_count]
    # ndi1= adxs.ndi[dmi_count]
    # adx1 = adxs.adx[dmi_count]

    # pdi2 = adxs.pdi[dmi_count-1]
    # ndi2 = adxs.ndi[dmi_count-1]
    # adx2 = adxs.adx[dmi_count-1]

    # pdi3 = adxs.pdi[dmi_count-2]
    # ndi3 = adxs.ndi[dmi_count-2]
    # adx3 = adxs.adx[dmi_count-2]

    # if pdi1>ndi1 and pdi2<ndi2:
    #     if(adx1>=23 and adx1>adx2 and adx2>adx3):
    #         print(bcolors.UP+"up adx signal"+bcolors.RESET)

    # elif pdi1<ndi1 and pdi2>ndi2:
    #     if(adx1>=23 and adx1>adx2 and adx2>adx3):
    #         print(bcolors.DOWN+"down adx signal"+bcolors.RESET)

    # if(adx1>=23 and adx2<23 and adx2>adx3):
    #     if pdi1>ndi1:
    #         print(bcolors.UP+"up adx signal"+bcolors.RESET)
    #     elif pdi1<ndi1:
    #         print(bcolors.DOWN+"down adx signal"+bcolors.RESET)
