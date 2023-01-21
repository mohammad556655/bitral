import schedule
from threading import Thread
import time
import os
import sys
import subprocess
print("starting server")
flag_15m=False
flag_30m=False
flag_1h=False
flag_4h=False
def start_15m():
    print('\n')
    print('\n')
    print('\n')
    print("start 15min")
    global flag_15m
    flag_15m = True
    return
def start_30m():
    global flag_30m
    flag_30m=True
    return
def start_1h():
    flag_1h=True
    return
def start_4h():
    flag_4h=True
    return
    



#15 minutes

# schedule.every(15).minutes.until("2030-01-01 03:15").do(start_15m)
# schedule.every(30).minutes.until("2030-01-01 03:15").do(start_30m)
# schedule.every(1).hour.until("2030-01-01 03:15").do(start_1h)
# schedule.every(4).hours.until("2030-01-01 03:15").do(start_4h)

# schedule.every().day.at("00:12").do(start_15m)
# schedule.every().day.at("00:27").do(start_15m)
# schedule.every().day.at("00:42").do(start_15m)
# schedule.every().day.at("00:57").do(start_15m)
# schedule.every().day.at("01:12").do(start_15m)
# schedule.every().day.at("01:27").do(start_15m)
# schedule.every().day.at("01:42").do(start_15m)
# schedule.every().day.at("01:57").do(start_15m)
# schedule.every().day.at("02:12").do(start_15m)
# schedule.every().day.at("02:27").do(start_15m)
# schedule.every().day.at("02:42").do(start_15m)
# schedule.every().day.at("02:57").do(start_15m)
# schedule.every().day.at("03:12").do(start_15m)
# schedule.every().day.at("03:27").do(start_15m)
# schedule.every().day.at("03:42").do(start_15m)
# schedule.every().day.at("03:57").do(start_15m)
# schedule.every().day.at("04:12").do(start_15m)
# schedule.every().day.at("04:27").do(start_15m)
# schedule.every().day.at("04:42").do(start_15m)
# schedule.every().day.at("04:57").do(start_15m)
# schedule.every().day.at("05:12").do(start_15m)
# schedule.every().day.at("05:27").do(start_15m)
# schedule.every().day.at("05:42").do(start_15m)
# schedule.every().day.at("05:57").do(start_15m)
# schedule.every().day.at("06:12").do(start_15m)
# schedule.every().day.at("06:27").do(start_15m)
# schedule.every().day.at("06:42").do(start_15m)
# schedule.every().day.at("06:57").do(start_15m)
# schedule.every().day.at("07:12").do(start_15m)
# schedule.every().day.at("07:27").do(start_15m)
# schedule.every().day.at("07:42").do(start_15m)
# schedule.every().day.at("07:57").do(start_15m)
# schedule.every().day.at("08:12").do(start_15m)
# schedule.every().day.at("08:27").do(start_15m)
# schedule.every().day.at("08:42").do(start_15m)
# schedule.every().day.at("08:57").do(start_15m)
# schedule.every().day.at("09:12").do(start_15m)
# schedule.every().day.at("09:27").do(start_15m)
# schedule.every().day.at("09:42").do(start_15m)
# schedule.every().day.at("09:57").do(start_15m)
# schedule.every().day.at("10:12").do(start_15m)
# schedule.every().day.at("10:27").do(start_15m)
# schedule.every().day.at("10:42").do(start_15m)
# schedule.every().day.at("10:57").do(start_15m)
# schedule.every().day.at("11:12").do(start_15m)
# schedule.every().day.at("11:27").do(start_15m)
# schedule.every().day.at("11:42").do(start_15m)
# schedule.every().day.at("11:57").do(start_15m)
# schedule.every().day.at("12:12").do(start_15m)
# schedule.every().day.at("12:27").do(start_15m)
# schedule.every().day.at("12:42").do(start_15m)
# schedule.every().day.at("12:57").do(start_15m)
# schedule.every().day.at("13:12").do(start_15m)
# schedule.every().day.at("13:27").do(start_15m)
# schedule.every().day.at("13:42").do(start_15m)
# schedule.every().day.at("13:57").do(start_15m)
# schedule.every().day.at("14:12").do(start_15m)
# schedule.every().day.at("14:27").do(start_15m)
# schedule.every().day.at("14:42").do(start_15m)
# schedule.every().day.at("14:57").do(start_15m)
# schedule.every().day.at("15:12").do(start_15m)
# schedule.every().day.at("15:27").do(start_15m)
# schedule.every().day.at("15:42").do(start_15m)
# schedule.every().day.at("15:57").do(start_15m)
# schedule.every().day.at("16:12").do(start_15m)
# schedule.every().day.at("16:27").do(start_15m)
# schedule.every().day.at("16:42").do(start_15m)
# schedule.every().day.at("16:57").do(start_15m)
# schedule.every().day.at("17:12").do(start_15m)
# schedule.every().day.at("17:27").do(start_15m)
# schedule.every().day.at("17:42").do(start_15m)
# schedule.every().day.at("17:57").do(start_15m)
# schedule.every().day.at("18:12").do(start_15m)
# schedule.every().day.at("18:27").do(start_15m)
# schedule.every().day.at("18:42").do(start_15m)
# schedule.every().day.at("18:57").do(start_15m)
# schedule.every().day.at("19:12").do(start_15m)
# schedule.every().day.at("19:27").do(start_15m)
# schedule.every().day.at("19:42").do(start_15m)
# schedule.every().day.at("19:57").do(start_15m)
# schedule.every().day.at("20:12").do(start_15m)
# schedule.every().day.at("20:27").do(start_15m)
# schedule.every().day.at("20:42").do(start_15m)
# schedule.every().day.at("20:57").do(start_15m)
# schedule.every().day.at("21:12").do(start_15m)
# schedule.every().day.at("21:27").do(start_15m)
# schedule.every().day.at("21:42").do(start_15m)
# schedule.every().day.at("21:57").do(start_15m)
# schedule.every().day.at("22:12").do(start_15m)
# schedule.every().day.at("22:27").do(start_15m)
# schedule.every().day.at("22:42").do(start_15m)
# schedule.every().day.at("22:57").do(start_15m)
# schedule.every().day.at("23:12").do(start_15m)
# schedule.every().day.at("23:27").do(start_15m)
# schedule.every().day.at("23:42").do(start_15m)
schedule.every().day.at("03:13").do(start_15m)
#
#
#
#
#
#
#
#
# #30 minutes
schedule.every().day.at("03:13").do(start_30m)
# schedule.every().day.at("00:56").do(start_30m)
# schedule.every().day.at("01:26").do(start_30m)
# schedule.every().day.at("01:56").do(start_30m)
# schedule.every().day.at("02:26").do(start_30m)
# schedule.every().day.at("02:56").do(start_30m)
# schedule.every().day.at("03:26").do(start_30m)
# schedule.every().day.at("03:56").do(start_30m)
# schedule.every().day.at("04:26").do(start_30m)
# schedule.every().day.at("04:56").do(start_30m)
# schedule.every().day.at("05:26").do(start_30m)
# schedule.every().day.at("05:56").do(start_30m)
# schedule.every().day.at("06:26").do(start_30m)
# schedule.every().day.at("06:56").do(start_30m)
# schedule.every().day.at("07:26").do(start_30m)
# schedule.every().day.at("07:56").do(start_30m)
# schedule.every().day.at("08:26").do(start_30m)
# schedule.every().day.at("08:56").do(start_30m)
# schedule.every().day.at("09:26").do(start_30m)
# schedule.every().day.at("09:56").do(start_30m)
# schedule.every().day.at("10:26").do(start_30m)
# schedule.every().day.at("10:56").do(start_30m)
# schedule.every().day.at("11:26").do(start_30m)
# schedule.every().day.at("11:56").do(start_30m)
# schedule.every().day.at("12:26").do(start_30m)
# schedule.every().day.at("12:56").do(start_30m)
# schedule.every().day.at("13:26").do(start_30m)
# schedule.every().day.at("13:56").do(start_30m)
# schedule.every().day.at("14:26").do(start_30m)
# schedule.every().day.at("14:56").do(start_30m)
# schedule.every().day.at("15:26").do(start_30m)
# schedule.every().day.at("15:56").do(start_30m)
# schedule.every().day.at("16:26").do(start_30m)
# schedule.every().day.at("16:56").do(start_30m)
# schedule.every().day.at("17:26").do(start_30m)
# schedule.every().day.at("17:56").do(start_30m)
# schedule.every().day.at("18:26").do(start_30m)
# schedule.every().day.at("18:56").do(start_30m)
# schedule.every().day.at("19:26").do(start_30m)
# schedule.every().day.at("19:56").do(start_30m)
# schedule.every().day.at("20:26").do(start_30m)
# schedule.every().day.at("20:56").do(start_30m)
# schedule.every().day.at("21:26").do(start_30m)
# schedule.every().day.at("21:56").do(start_30m)
# schedule.every().day.at("22:26").do(start_30m)
# schedule.every().day.at("22:56").do(start_30m)
# schedule.every().day.at("23:26").do(start_30m)
# schedule.every().day.at("23:56").do(start_30m)
#
#
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
#
# schedule.every().day.at("03:20").do(start_4h)
# schedule.every().day.at("07:20").do(start_4h)
# schedule.every().day.at("11:20").do(start_4h)
# schedule.every().day.at("15:20").do(start_4h)
# schedule.every().day.at("19:20").do(start_4h)
# schedule.every().day.at("23:20").do(start_4h)

while True:
    schedule.run_pending()
    print(flag_15m)
    child1=
    child2=
    if(flag_15m==True):
        child1 = subprocess.Popen([sys.executable, '.\Scripts\python.exe ramin_cmo.py 15m'])
        # Thread(target=os.system('.\Scripts\python.exe ramin_cmo.py 15m')).start()
    if(flag_30m==True):
        child2 = subprocess.Popen([sys.executable, '.\Scripts\python.exe ramin_cmo.py 30m'])
        # Thread(target=os.system('.\Scripts\python.exe ramin_cmo.py 30m')).start()
    if(flag_1h==True):
        Thread(target=os.system('.\Scripts\python.exe ramin_cmo.py 1h')).start()
    if(flag_4h==True):
        Thread(target=os.system('.\Scripts\python.exe ramin_cmo.py 4h')).start()
    flag_15m=False
    flag_30m=False
    flag_1h=False
    flag_4h=False
    child1.wait()
    child2.wait()
    time.sleep(30) # wait HALF minute