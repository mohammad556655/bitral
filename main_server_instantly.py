from tempfile import TemporaryDirectory
import schedule
import time
import os
from test import get_data
from ramin_cmo_for_instant import analyze
import pandas as pd
pairs=['BTC-USDT','ETH-USDT']



first_run = True


def every_10_second():
    global ohlc
    global first_run

    print("start 15min")
    if(first_run == True):
        for pair in pairs:
            ohlc = get_data(pair,timeframe='15m',limit=500)
            ohlc.to_csv(f'ohlc_data/{pair}_15m.csv') 
            analyze(ohlc,timeframe='15m')
        first_run = False
    else:
        for pair in pairs:
            print('\n')
            print('\n')
            print('\n')
            ohlc = pd.read_csv(f'ohlc_data/{pair}_15m.csv')  
            ohlc = ohlc.set_index('date')
            print(ohlc)
            temp_ohlc = get_data(pair,timeframe='15m',limit=1)
            ohlc = ohlc.iloc[:-1,:]
            ohlc = pd.concat([ohlc, temp_ohlc])
            print(ohlc)
            analyze(ohlc,timeframe='15m')
    return
def start_15m():
    global ohlc
    for pair in pairs:
        ohlc = get_data(pair,timeframe='15m',limit=500)
        ohlc.to_csv(f'ohlc_data/{pair}_15m.csv') 
    # os.system('.\Scripts\python.exe mina_ichi_macd_ema.py 30m')
    return
# def start_1h():
#     os.system('.\Scripts\python.exe ramin_cmo.py 1h')
#     os.system('.\Scripts\python.exe rsi+ema200+sar.py')
#     return
# def start_4h():
#     os.system('.\Scripts\python.exe ramin_cmo.py 4h')
#     # os.system('.\Scripts\python.exe mina_ichi_macd_ema.py 4h')
    return


schedule.every(10).seconds.do(every_10_second)

# 15 minutes
schedule.every().day.at("00:12").do(start_15m)
schedule.every().day.at("00:27").do(start_15m)
schedule.every().day.at("00:42").do(start_15m)
schedule.every().day.at("00:57").do(start_15m)
schedule.every().day.at("01:12").do(start_15m)
schedule.every().day.at("01:27").do(start_15m)
schedule.every().day.at("01:42").do(start_15m)
schedule.every().day.at("01:57").do(start_15m)
schedule.every().day.at("02:12").do(start_15m)
schedule.every().day.at("02:27").do(start_15m)
schedule.every().day.at("02:42").do(start_15m)
schedule.every().day.at("02:57").do(start_15m)
schedule.every().day.at("03:12").do(start_15m)
schedule.every().day.at("03:27").do(start_15m)
schedule.every().day.at("03:42").do(start_15m)
schedule.every().day.at("03:57").do(start_15m)
schedule.every().day.at("04:12").do(start_15m)
schedule.every().day.at("04:27").do(start_15m)
schedule.every().day.at("04:42").do(start_15m)
schedule.every().day.at("04:57").do(start_15m)
schedule.every().day.at("05:12").do(start_15m)
schedule.every().day.at("05:27").do(start_15m)
schedule.every().day.at("05:42").do(start_15m)
schedule.every().day.at("05:57").do(start_15m)
schedule.every().day.at("06:12").do(start_15m)
schedule.every().day.at("06:27").do(start_15m)
schedule.every().day.at("06:42").do(start_15m)
schedule.every().day.at("06:57").do(start_15m)
schedule.every().day.at("07:12").do(start_15m)
schedule.every().day.at("07:27").do(start_15m)
schedule.every().day.at("07:42").do(start_15m)
schedule.every().day.at("07:57").do(start_15m)
schedule.every().day.at("08:12").do(start_15m)
schedule.every().day.at("08:27").do(start_15m)
schedule.every().day.at("08:42").do(start_15m)
schedule.every().day.at("08:57").do(start_15m)
schedule.every().day.at("09:12").do(start_15m)
schedule.every().day.at("09:27").do(start_15m)
schedule.every().day.at("09:42").do(start_15m)
schedule.every().day.at("09:57").do(start_15m)
schedule.every().day.at("10:12").do(start_15m)
schedule.every().day.at("10:27").do(start_15m)
schedule.every().day.at("10:42").do(start_15m)
schedule.every().day.at("10:57").do(start_15m)
schedule.every().day.at("11:12").do(start_15m)
schedule.every().day.at("11:27").do(start_15m)
schedule.every().day.at("11:42").do(start_15m)
schedule.every().day.at("11:57").do(start_15m)
schedule.every().day.at("12:12").do(start_15m)
schedule.every().day.at("12:27").do(start_15m)
schedule.every().day.at("12:42").do(start_15m)
schedule.every().day.at("12:57").do(start_15m)
schedule.every().day.at("13:12").do(start_15m)
schedule.every().day.at("13:27").do(start_15m)
schedule.every().day.at("13:42").do(start_15m)
schedule.every().day.at("13:57").do(start_15m)
schedule.every().day.at("14:12").do(start_15m)
schedule.every().day.at("14:27").do(start_15m)
schedule.every().day.at("14:42").do(start_15m)
schedule.every().day.at("14:57").do(start_15m)
schedule.every().day.at("15:12").do(start_15m)
schedule.every().day.at("15:27").do(start_15m)
schedule.every().day.at("15:42").do(start_15m)
schedule.every().day.at("15:57").do(start_15m)
schedule.every().day.at("16:12").do(start_15m)
schedule.every().day.at("16:27").do(start_15m)
schedule.every().day.at("16:42").do(start_15m)
schedule.every().day.at("16:57").do(start_15m)
schedule.every().day.at("17:12").do(start_15m)
schedule.every().day.at("17:27").do(start_15m)
schedule.every().day.at("17:42").do(start_15m)
schedule.every().day.at("17:57").do(start_15m)
schedule.every().day.at("18:12").do(start_15m)
schedule.every().day.at("18:27").do(start_15m)
schedule.every().day.at("18:42").do(start_15m)
schedule.every().day.at("18:57").do(start_15m)
schedule.every().day.at("19:12").do(start_15m)
schedule.every().day.at("19:27").do(start_15m)
schedule.every().day.at("19:42").do(start_15m)
schedule.every().day.at("19:57").do(start_15m)
schedule.every().day.at("20:12").do(start_15m)
schedule.every().day.at("20:27").do(start_15m)
schedule.every().day.at("20:42").do(start_15m)
schedule.every().day.at("20:57").do(start_15m)
schedule.every().day.at("21:12").do(start_15m)
schedule.every().day.at("21:27").do(start_15m)
schedule.every().day.at("21:42").do(start_15m)
schedule.every().day.at("21:57").do(start_15m)
schedule.every().day.at("22:12").do(start_15m)
schedule.every().day.at("22:27").do(start_15m)
schedule.every().day.at("22:42").do(start_15m)
schedule.every().day.at("22:57").do(start_15m)
schedule.every().day.at("23:12").do(start_15m)
schedule.every().day.at("23:27").do(start_15m)
schedule.every().day.at("23:42").do(start_15m)
schedule.every().day.at("23:57").do(start_15m)








# #30 minutes
# schedule.every().day.at("00:25").do(start_30m)
# schedule.every().day.at("00:55").do(start_30m)
# schedule.every().day.at("01:25").do(start_30m)
# schedule.every().day.at("01:55").do(start_30m)
# schedule.every().day.at("02:25").do(start_30m)
# schedule.every().day.at("02:55").do(start_30m)
# schedule.every().day.at("03:25").do(start_30m)
# schedule.every().day.at("03:55").do(start_30m)
# schedule.every().day.at("04:25").do(start_30m)
# schedule.every().day.at("04:55").do(start_30m)
# schedule.every().day.at("05:25").do(start_30m)
# schedule.every().day.at("05:55").do(start_30m)
# schedule.every().day.at("06:25").do(start_30m)
# schedule.every().day.at("06:55").do(start_30m)
# schedule.every().day.at("07:25").do(start_30m)
# schedule.every().day.at("07:55").do(start_30m)
# schedule.every().day.at("08:25").do(start_30m)
# schedule.every().day.at("08:55").do(start_30m)
# schedule.every().day.at("09:25").do(start_30m)
# schedule.every().day.at("09:55").do(start_30m)
# schedule.every().day.at("10:25").do(start_30m)
# schedule.every().day.at("10:55").do(start_30m)
# schedule.every().day.at("11:25").do(start_30m)
# schedule.every().day.at("11:55").do(start_30m)
# schedule.every().day.at("12:25").do(start_30m)
# schedule.every().day.at("12:55").do(start_30m)
# schedule.every().day.at("13:25").do(start_30m)
# schedule.every().day.at("13:55").do(start_30m)
# schedule.every().day.at("14:25").do(start_30m)
# schedule.every().day.at("14:55").do(start_30m)
# schedule.every().day.at("15:25").do(start_30m)
# schedule.every().day.at("15:55").do(start_30m)
# schedule.every().day.at("16:25").do(start_30m)
# schedule.every().day.at("16:55").do(start_30m)
# schedule.every().day.at("17:25").do(start_30m)
# schedule.every().day.at("17:55").do(start_30m)
# schedule.every().day.at("18:25").do(start_30m)
# schedule.every().day.at("18:55").do(start_30m)
# schedule.every().day.at("19:25").do(start_30m)
# schedule.every().day.at("19:55").do(start_30m)
# schedule.every().day.at("20:25").do(start_30m)
# schedule.every().day.at("20:55").do(start_30m)
# schedule.every().day.at("21:25").do(start_30m)
# schedule.every().day.at("21:55").do(start_30m)
# schedule.every().day.at("22:25").do(start_30m)
# schedule.every().day.at("22:55").do(start_30m)
# schedule.every().day.at("23:25").do(start_30m)
# schedule.every().day.at("23:55").do(start_30m)


# schedule.every().day.at("00:25").do(start_1h)
# schedule.every().day.at("01:25").do(start_1h)
# schedule.every().day.at("02:25").do(start_1h)
# schedule.every().day.at("03:25").do(start_1h)
# schedule.every().day.at("04:25").do(start_1h)
# schedule.every().day.at("05:25").do(start_1h)
# schedule.every().day.at("06:25").do(start_1h)
# schedule.every().day.at("07:25").do(start_1h)
# schedule.every().day.at("08:25").do(start_1h)
# schedule.every().day.at("09:25").do(start_1h)
# schedule.every().day.at("10:25").do(start_1h)
# schedule.every().day.at("11:25").do(start_1h)
# schedule.every().day.at("12:25").do(start_1h)
# schedule.every().day.at("13:25").do(start_1h)
# schedule.every().day.at("14:25").do(start_1h)
# schedule.every().day.at("15:25").do(start_1h)
# schedule.every().day.at("16:25").do(start_1h)
# schedule.every().day.at("17:25").do(start_1h)
# schedule.every().day.at("18:25").do(start_1h)
# schedule.every().day.at("19:25").do(start_1h)
# schedule.every().day.at("20:25").do(start_1h)
# schedule.every().day.at("21:25").do(start_1h)
# schedule.every().day.at("22:25").do(start_1h)
# schedule.every().day.at("23:25").do(start_1h)

# schedule.every().day.at("03:20").do(start_4h)
# schedule.every().day.at("07:20").do(start_4h)
# schedule.every().day.at("11:20").do(start_4h)
# schedule.every().day.at("15:20").do(start_4h)
# schedule.every().day.at("19:20").do(start_4h)
# schedule.every().day.at("23:20").do(start_4h)

while True:
    schedule.run_pending()
    
    time.sleep(10) # wait ten second