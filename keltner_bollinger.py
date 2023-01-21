from analyzers import bollinger
from analyzers import willr
from analyzers import rsi
from analyzers import ichimoku
from analyzers import stochastic
from test import get_data
from send_to_channel import send
import time
from analyzers import adx
from analyzers import keltner
import heikin_ashi 
from datetime import datetime
import pytz



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
timeframe='15m' 
tz_London = pytz.timezone('Europe/London')
now = datetime.now(tz_London)
rsi = rsi.RSI()

current_time = now.strftime("%d/%m/%Y %H:%M:%S")

for pair in pairs:
    # adxs = adx.Adx()
    ohlc =get_data(pair,timeframe)
    heikin = heikin_ashi.make_heikin(ohlc=ohlc)

    rsis = rsi.analyze(heikin,4)
    # ichim=ichimoku.Ichimoku()
    # ichimokus = ichim.analyze(heikin)
    middlekelt, upperkelt,lowerkelt = keltner.get_kc(heikin.high, heikin.low,heikin.close, 20, 2, 10)



    bollinger_bands = bollinger.Bollinger()
    bollingers = bollinger_bands.analyze(heikin)
    
    # ichi_count = ichimokus.shape[0]-1
    # Dmi = adxs.analyze(ohlc,14)
    bollinger_count = bollingers.shape[0]-1

    rsi_count = rsis.shape[0]-1

    # dmi_count = Dmi.shape[0]-1
    # ohlc_count = ohlc.shape[0]-1
    # close1 = ohlc.close[ohlc_count]
    # close2 = ohlc.close[ohlc_count-1]
    # close3 = ohlc.close[ohlc_count-2]
    # close4 = ohlc.close[ohlc_count-3]
    # close5 = ohlc.close[ohlc_count-4]

    # adx1 = Dmi.adx[dmi_count]
    # adx2 = Dmi.adx[dmi_count-1]
    # adx3 = Dmi.adx[dmi_count-2]
    # adx4 = Dmi.adx[dmi_count-3]
    # adx5 = Dmi.adx[dmi_count-4]


    rsi1 = rsis.rsi[rsi_count]
    rsi2 = rsis.rsi[rsi_count-1]
    rsi3 = rsis.rsi[rsi_count-2]
    rsi4 = rsis.rsi[rsi_count-3]
    rsi5 = rsis.rsi[rsi_count-4]
    rsi6 = rsis.rsi[rsi_count-5]

    upband1 = bollingers.up_band[bollinger_count]
    upband2 = bollingers.up_band[bollinger_count-1]
    upband3 = bollingers.up_band[bollinger_count-2]
    upband4 = bollingers.up_band[bollinger_count-3]
    upband5 = bollingers.up_band[bollinger_count-4] 

    lowband1 = bollingers.low_band[bollinger_count]
    lowband2 = bollingers.low_band[bollinger_count-1]
    lowband3 = bollingers.low_band[bollinger_count-2]
    lowband4 = bollingers.low_band[bollinger_count-3]
    lowband5 = bollingers.low_band[bollinger_count-4]


    # chico1 = ichimokus.chikou_span[ichi_count]
    # chico2 = ichimokus.chikou_span[ichi_count-1]
    # chico3 = ichimokus.chikou_span[ichi_count-2]
    # chico4 = ichimokus.chikou_span[ichi_count-3]
    # chico5 = ichimokus.chikou_span[ichi_count-4]
    # chico6 = ichimokus.chikou_span[ichi_count-5]

    # willr1 = willrs.willr[willr_count]
    # willr2 = willrs.willr[willr_count-1]
    # willr3 = willrs.willr[willr_count-2]
    # willr4 = willrs.willr[willr_count-3]
    # willr5 = willrs.willr[willr_count-4]
    # willr6 = willrs.willr[willr_count-5]

    # k1 = stoch.slowk[stoch_count]
    # k2 = stoch.slowk[stoch_count-1]
    # k3 = stoch.slowk[stoch_count-2]
    # k4 = stoch.slowk[stoch_count-3]
    # k5 = stoch.slowk[stoch_count-4]
    # k6 = stoch.slowk[stoch_count-5]
    
    # d1 = stoch.slowd[stoch_count]
    # d2 = stoch.slowd[stoch_count-1]
    # d3 = stoch.slowd[stoch_count-2]
    # d4 = stoch.slowd[stoch_count-3]
    # d5 = stoch.slowd[stoch_count-4]
    # d6 = stoch.slowd[stoch_count-5]

    message=""

    # 1th candle
    if(rsi2<70 and rsi1>=70):
        if(lowerkelt[-1]>lowband1):
            if(upperkelt[-1]<upband1):
                print(bcolors.UP+"up signal signal with kelttner strategy"+bcolors.RESET)
                print(bcolors.UP+"price is: "+str(ohlc.close[-1])+bcolors.RESET)
                message = pair+"\n"+"TIME:"+current_time+"\n"+"time frame: "+str(timeframe)+"\n"+"BUY signal with keltner strategy"+"\n"+"price is: "+str(ohlc.close[-1])+"\n"
                send(message)


    elif(rsi2>30 and rsi1<=30):
        if(lowerkelt[-1]>lowband1):
            if(upperkelt[-1]<upband1):
                print(bcolors.DOWN+"down signal with keltner strategy"+bcolors.RESET)
                print(bcolors.DOWN+"price is: "+str(ohlc.close[-1])+bcolors.RESET)
                message = pair+"\n"+"TIME:"+current_time+"\n"+"time frame: "+str(timeframe)+"\n"+"SELL signal with keltner strategy"+"\n"+"price is: "+str(ohlc.close[-1])+"\n"
                send(message)


    message=""



