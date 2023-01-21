from curses import KEY_A1
from analyzers import bollinger
from operator import truediv
from analyzers import willr
from analyzers import rsi
from analyzers import ichimoku
from analyzers import stochastic
from analyzers import adx
from test import get_data
from send_to_channel import send
import time
import cufflinks as cf
pairs=['BTC-USDT','ETH-USDT','ADA-USDT','AXS-USDT','SOL-USDT','IOST-USDT','FLOW-USDT','IOTX-USDT','XMR-USDT','ETC-USDT','XTZ-USDT'
        ,'EGLD-USDT','SAND-USDT','ADA-USDT','XRP-USDT','CAKE-USDT','DOGE-USDT','DOT-USDT','AVAX-USDT','MATIC-USDT'
        ,'ALGO-USDT','ICP-USDT','VET-USDT','AAVE-USDT','AXS-USDT','UNI-USDT','FIL-USDT','SHIB-USDT','EOS-USDT','KCS-USDT'
        ,'LTC-USDT','ATOM-USDT','LINK-USDT','BCH-USDT','TRX-USDT','XLM-USDT','MANA-USDT','HBAR-USDT','APE-USDT','FTM-USDT','GRT-USDT'
        ,'THETA-USDT','MKR-USDT','DYP-USDT']
class bcolors:
    OK = '\033[92m' #GREEN
    DOWN = '\033[93m' #YELLOW
    UP = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR 
timeframe='30m' 
while True:
    for pair in pairs:
        adxs = adx.Adx()

        ohlc =get_data(pair,timeframe)
        stoch = stochastic.STOCH.analyze(ohlc)
        willrs=willr.willr(ohlc,14)
        rsis = rsi.RSI.analyze(ohlc,14)
        ichim=ichimoku.Ichimoku()
        ichimokus = ichim.analyze(ohlc)
        Dmi = adxs.analyze(ohlc,14)

        bollinger_bands = bollinger.Bollinger()
        bollingers = bollinger_bands.analyze(ohlc)
        
        ichi_count = ichimokus.shape[0]-1

        dmi_count = Dmi.shape[0]-1

        bollinger_count = bollingers.shape[0]-1

        rsi_count = rsis.shape[0]-1

        willr_count = willrs.shape[0]-1

        stoch_count = stoch.shape[0]-1
        ohlc_count = ohlc.shape[0]-1

        adx1 = Dmi.adx[dmi_count]
        adx2 = Dmi.adx[dmi_count-1]
        adx3 = Dmi.adx[dmi_count-2]
        adx4 = Dmi.adx[dmi_count-3]
        adx5 = Dmi.adx[dmi_count-4]




        close1 = ohlc.close[ohlc_count]
        close2 = ohlc.close[ohlc_count-1]
        close3 = ohlc.close[ohlc_count-2]
        close4 = ohlc.close[ohlc_count-3]
        close5 = ohlc.close[ohlc_count-4]


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


        chico1 = ichimokus.chikou_span[ichi_count]
        chico2 = ichimokus.chikou_span[ichi_count-1]
        chico3 = ichimokus.chikou_span[ichi_count-2]
        chico4 = ichimokus.chikou_span[ichi_count-3]
        chico5 = ichimokus.chikou_span[ichi_count-4]
        chico6 = ichimokus.chikou_span[ichi_count-5]

        willr1 = willrs.willr[willr_count]
        willr2 = willrs.willr[willr_count-1]
        willr3 = willrs.willr[willr_count-2]
        willr4 = willrs.willr[willr_count-3]
        willr5 = willrs.willr[willr_count-4]
        willr6 = willrs.willr[willr_count-5]

        k1 = stoch.slowk[stoch_count]
        k2 = stoch.slowk[stoch_count-1]
        k3 = stoch.slowk[stoch_count-2]
        k4 = stoch.slowk[stoch_count-3]
        k5 = stoch.slowk[stoch_count-4]
        k6 = stoch.slowk[stoch_count-5]
        
        
        
        d1 = stoch.slowd[stoch_count]
        d2 = stoch.slowd[stoch_count-1]
        d3 = stoch.slowd[stoch_count-2]
        d4 = stoch.slowd[stoch_count-3]
        d5 = stoch.slowd[stoch_count-4]
        d6 = stoch.slowd[stoch_count-5]

        print("rsi :"+str(rsi1))
        print("chico :"+str(chico1))
        print("willr :"+str(willr1))
        print("k1 :"+str(k1))
        print("d1 :"+str(d1))
        message=""

        # 1th candle
        if(willr1<willr2 and willr3<willr2 and willr2>-10):
            if(rsi1>=60 and rsi1>rsi2):
                if(d1>k1 and d2<k2 and d2>=80 and k2>=80):
                    if close1>=upband1:
                        #if(adx1>=32 or adx1<=18):
                            print(bcolors.DOWN+"down signal 1th candle"+bcolors.RESET)
                            print(bcolors.DOWN+"price is: "+str(close1)+bcolors.RESET)
                                
                            message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"SELL signal 1th candle"+"\n"+"price is: "+str(close1)+"\n"+"adx is:"+str(adx1)

                            send(message)


        elif(willr1>willr2 and willr3>willr2 and willr2<-90 ):
            if(rsi1<=40 and rsi1<rsi2):
                if(d1<k1 and d2>k2 and d2<=20 and k2<=20):
                    if(close1<=lowband1):
                        #if(adx1>=32 or adx1<=18):
                            print(bcolors.UP+"up signal 1th candle"+bcolors.RESET)
                            print(bcolors.UP+"price is: "+str(close1)+bcolors.RESET)
                            message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"BUY signal 1th candle"+"\n"+"price is: "+str(close1)+"\n"+"adx is:"+str(adx1)

                            send(message)


        # message=""
        # rsi_checked=False




        # #2th candle
        # if(willr2<willr3 and willr4<willr3 and willr3>-10):
        #     if(rsi2>=60 and rsi2>rsi3):
        #         if(d2>k2 and d3<k3 and d3>=80 and k3>=80):
        #             if close2>=upband2 or close1>=upband1:
        #                 print(bcolors.DOWN+"down signal 2th candle"+bcolors.RESET)
        #                 print(bcolors.DOWN+"price is: "+str(close2)+bcolors.RESET)
        #                 if(rsi_checked==True):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"SELL signal 2th candle"+"\n"+"price is: "+str(close2)+"\n"+"rsi checked"
                            
        #                 elif(rsi_checked==False):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"SELL signal 2th candle"+"\n"+"price is: "+str(close2)

        #                 send(message)
        # elif(willr2>willr3 and willr4>willr3 and willr3<-90 ):
        #     if(rsi2<=40 and rsi2<rsi3):
        #         if(d2<k2 and d3>k3 and d3<=20 and k3<=20):
        #             if(close2<=lowband2 or close1<=lowband1):
        #                 print(bcolors.UP+"up signal 2th candle"+bcolors.RESET)
        #                 print(bcolors.up+"price is: "+str(close2)+bcolors.RESET)
        #                 if(rsi_checked==True):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"BUY signal 2th candle"+"\n"+"price is: "+str(close2)+"\n"+"rsi checked"
                            
        #                 elif(rsi_checked==False):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"BUY signal 2th candle"+"\n"+"price is: "+str(close2)

        #                 send(message)



        # message=""
        # rsi_checked=False




        # #3th candle
        # if(willr3<willr4 and willr5<willr4 and willr4>-10):
        #     if(rsi3>=60 and rsi3>rsi4):
        #         if(d3>k3 and d4<k4 and d4>=80 and k4>=80):
        #             if close2>=upband2 or close1>=upband1:
        #                 print(bcolors.DOWN+"down signal 3th candle"+bcolors.RESET)
        #                 print(bcolors.DOWN+"price is: "+str(close3)+bcolors.RESET)
        #                 if(rsi_checked==True):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"SELL signal 3th candle"+"\n"+"price is: "+str(close3)+"\n"+"rsi checked"
                            
        #                 elif(rsi_checked==False):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"SELL signal 3th candle"+"\n"+"price is: "+str(close3)

        #                 send(message)
        # elif(willr3>willr4 and willr5>willr4 and willr4<-90 ):
        #     if(rsi3<=40 and rsi3<rsi4):
        #         if(d3<k3 and d4>k4 and d4<=20 and k4<=20):
        #             if(close2<=lowband2 or close1<=lowband1):
        #                 print(bcolors.UP+"up signal 3th candle"+bcolors.RESET)
        #                 print(bcolors.up+"price is: "+str(close3)+bcolors.RESET)
        #                 if(rsi_checked==True):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"BUY signal 3th candle"+"\n"+"price is: "+str(close3)+"\n"+"rsi checked"
                            
        #                 elif(rsi_checked==False):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"BUY signal 3th candle"+"\n"+"price is: "+str(close3)

        #                 send(message)





        # message=""
        # rsi_checked=False



        # # 4th candle
        # if(willr3<willr5 and willr6<willr5 and willr5>-10):
        #     if(rsi4>=60 and rsi4>rsi5):
        #         if(d4>k4 and d5<k5 and d5>=80 and k5>=80):
        #             if close2>=upband2 or close1>=upband1:
        #                 print(bcolors.DOWN+"down signal 4th candle"+bcolors.RESET)
        #                 print(bcolors.DOWN+"price is: "+str(close4)+bcolors.RESET)
        #                 if(rsi_checked==True):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"SELL signal 4th candle"+"\n"+"price is: "+str(close4)+"\n"+"rsi checked"
                            
        #                 elif(rsi_checked==False):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"SELL signal 4th candle"+"\n"+"price is: "+str(close4)

        #                 send(message)
        # elif(willr4>willr5 and willr6>willr5 and willr5<-90 ):
        #     if(rsi4<=40 and rsi4<rsi5):
        #         if(d4<k4 and d5>k5 and d5<=20 and k5<=20):
        #             if(close2<=lowband2 or close1<=lowband1):
        #                 print(bcolors.UP+"up signal with 4th candle"+bcolors.RESET)
        #                 print(bcolors.up+"price is: "+str(close4)+bcolors.RESET)
        #                 if(rsi_checked==True):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"BUY signal 4th candle"+"\n"+"price is: "+str(close4)+"\n"+"rsi checked"
                            
        #                 elif(rsi_checked==False):
        #                     message = pair+"\n"+"time frame: "+str(timeframe)+"\n"+"BUY signal 4th candle"+"\n"+"price is: "+str(close4)

        #                 send(message)  
    print("\n\n"+"sleep for 30 min")  
    time.sleep(1800)        
