import pandas as pd
from datetime import datetime
from test import get_data
from analyzers import lsma
import heikin_ashi
from send_to_channel import send
from analyzers import bbp
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
timeframe='1h' 
tz_London = pytz.timezone('Europe/London')
now = datetime.now(tz_London)

current_time = now.strftime("%d/%m/%Y %H:%M:%S")
for pair in pairs:
    x = bbp.BBP()
    ohlc =get_data(pair,timeframe)
    heikin = heikin_ashi.make_heikin(ohlc=ohlc)
    lsmas=lsma.analyze(heikin,l1=20,offset=8)
    bbps = x.analyze(heikin,period_count=200)
    lsma_count = lsmas.shape[0]-1
    heikin_count = heikin.shape[0]-1
    bbp_count = bbps.shape[0]-1

    
    close1 = heikin.close[heikin_count]
    close2 = heikin.close[heikin_count-1]
    close3 = heikin.close[heikin_count-2]
    
    bbp1 = bbps.bbp[bbp_count]
    bbp2 = bbps.bbp[bbp_count-1]
    bbp3 = bbps.bbp[bbp_count-2]

    lsma1 = lsmas.lsma[lsma_count]
    lsma2 = lsmas.lsma[lsma_count-1]
    lsma3 = lsmas.lsma[lsma_count-2]
    print(bbp1)
    print(bbp2)
    if close1 > lsma1:
        if(bbp1>1 and bbp2<=1 and bbp1>bbp2) or (bbp1>0 and bbp2<=0 and bbp1>bbp2):
            print(bcolors.UP+"up signal"+bcolors.RESET)
            print(bcolors.UP+"price is: "+str(close1)+bcolors.RESET)
            message = pair+"\n"+"TIME:"+current_time+"\n"+"time frame: "+str(timeframe)+"\n"+"BUY signal with bbp and lsma strategy"+"\n"+"price is: "+str(close1)+"\n"
            send(message)
    elif close1<lsma1:
        if (bbp2>=1 and bbp1<1 and bbp1<bbp2) or (bbp2>=0 and bbp1<0 and bbp1<bbp2):
            print(bcolors.DOWN+"down signal"+bcolors.RESET)
            print(bcolors.DOWN+"price is: "+str(close1)+bcolors.RESET)            
            message = pair+"\n"+"TIME:"+current_time+"\n"+"time frame: "+str(timeframe)+"\n"+"SELL signal with bbp and lsma strategy"+"\n"+"price is: "+str(close1)+"\n"
            send(message)

    