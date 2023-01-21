import schedule
import time
import os
print("starting server for bbp and lsma 30m")

def start_bbp15m():
    os.system('python lsma_bbp15m.py')
    return
def start_bbp30m():
    os.system('python lsma_bbp30m.py')
    return
def start_bbp1h():
    os.system('python lsma_bbp1h.py')
    return
def start_bbp4h():
    os.system('python lsma_bbp4h.py')
    return
schedule.every().day.at("00:26").do(start_bbp30m)
schedule.every().day.at("00:56").do(start_bbp30m)
schedule.every().day.at("01:26").do(start_bbp30m)
schedule.every().day.at("01:56").do(start_bbp30m)
schedule.every().day.at("02:26").do(start_bbp30m)
schedule.every().day.at("02:56").do(start_bbp30m)
schedule.every().day.at("03:26").do(start_bbp30m)
schedule.every().day.at("03:56").do(start_bbp30m)
schedule.every().day.at("04:26").do(start_bbp30m)
schedule.every().day.at("04:56").do(start_bbp30m)
schedule.every().day.at("05:26").do(start_bbp30m)
schedule.every().day.at("05:56").do(start_bbp30m)
schedule.every().day.at("06:26").do(start_bbp30m)
schedule.every().day.at("06:56").do(start_bbp30m)
schedule.every().day.at("07:26").do(start_bbp30m)
schedule.every().day.at("07:56").do(start_bbp30m)
schedule.every().day.at("08:26").do(start_bbp30m)
schedule.every().day.at("08:56").do(start_bbp30m)
schedule.every().day.at("09:26").do(start_bbp30m)
schedule.every().day.at("09:56").do(start_bbp30m)
schedule.every().day.at("10:26").do(start_bbp30m)
schedule.every().day.at("10:56").do(start_bbp30m)
schedule.every().day.at("11:26").do(start_bbp30m)
schedule.every().day.at("11:56").do(start_bbp30m)
schedule.every().day.at("12:26").do(start_bbp30m)
schedule.every().day.at("12:56").do(start_bbp30m)
schedule.every().day.at("13:26").do(start_bbp30m)
schedule.every().day.at("13:56").do(start_bbp30m)
schedule.every().day.at("14:26").do(start_bbp30m)
schedule.every().day.at("14:56").do(start_bbp30m)
schedule.every().day.at("15:26").do(start_bbp30m)
schedule.every().day.at("15:56").do(start_bbp30m)
schedule.every().day.at("16:26").do(start_bbp30m)
schedule.every().day.at("16:56").do(start_bbp30m)
schedule.every().day.at("17:26").do(start_bbp30m)
schedule.every().day.at("17:56").do(start_bbp30m)
schedule.every().day.at("18:26").do(start_bbp30m)
schedule.every().day.at("18:56").do(start_bbp30m)
schedule.every().day.at("19:26").do(start_bbp30m)
schedule.every().day.at("19:56").do(start_bbp30m)
schedule.every().day.at("20:26").do(start_bbp30m)
schedule.every().day.at("20:56").do(start_bbp30m)
schedule.every().day.at("21:26").do(start_bbp30m)
schedule.every().day.at("21:56").do(start_bbp30m)
schedule.every().day.at("22:26").do(start_bbp30m)
schedule.every().day.at("22:56").do(start_bbp30m)
schedule.every().day.at("23:26").do(start_bbp30m)
schedule.every().day.at("23:56").do(start_bbp30m)


while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute