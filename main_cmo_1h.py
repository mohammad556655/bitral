import schedule
import time
import os

def start_ramin_1h():
    print('ramin started')
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    os.system('c:/Users/moham/Desktop/app/robot/Scripts/python.exe c:/Users/moham/Desktop/app/robot/forex_ramin_cmo.py 1h')
    return



schedule.every().day.at("00:25").do(start_ramin_1h)
schedule.every().day.at("01:25").do(start_ramin_1h)
schedule.every().day.at("02:25").do(start_ramin_1h)
schedule.every().day.at("03:25").do(start_ramin_1h)
schedule.every().day.at("04:25").do(start_ramin_1h)
schedule.every().day.at("05:25").do(start_ramin_1h)
schedule.every().day.at("06:25").do(start_ramin_1h)
schedule.every().day.at("07:25").do(start_ramin_1h)
schedule.every().day.at("08:25").do(start_ramin_1h)
schedule.every().day.at("09:25").do(start_ramin_1h)
schedule.every().day.at("10:25").do(start_ramin_1h)
schedule.every().day.at("11:25").do(start_ramin_1h)
schedule.every().day.at("12:25").do(start_ramin_1h)
schedule.every().day.at("13:25").do(start_ramin_1h)
schedule.every().day.at("14:25").do(start_ramin_1h)
schedule.every().day.at("15:25").do(start_ramin_1h)
schedule.every().day.at("16:25").do(start_ramin_1h)
schedule.every().day.at("17:25").do(start_ramin_1h)
schedule.every().day.at("18:25").do(start_ramin_1h)
schedule.every().day.at("19:25").do(start_ramin_1h)
schedule.every().day.at("20:25").do(start_ramin_1h)
schedule.every().day.at("21:25").do(start_ramin_1h)
schedule.every().day.at("22:25").do(start_ramin_1h)
schedule.every().day.at("23:25").do(start_ramin_1h)


while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute