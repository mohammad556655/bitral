import telegram
from tenacity import retry, retry_if_exception_type, stop_after_attempt

import time

bot = telegram.Bot(token='5135949153:AAFr8IZwDOGtCxIX1by6_VGrkFm-3d62tuY')
#@retry(retry=retry_if_exception_type(telegram.error.RetryAfter),stop=stop_after_attempt(10))
def send_main(msg):

    message=msg
    if(message!=''):
        time.sleep(2) # Sleep for 3 seconds
        status = bot.send_message(chat_id='@trading_officials', text=message, parse_mode=telegram.ParseMode.HTML)
    else:
        print("message is empty...........................................")

def send_ramin(msg):

    message=msg
    if(message!=''):
        time.sleep(2) # Sleep for 3 seconds
        status = bot.send_message(chat_id='@ramin_tradingofficials', text=message, parse_mode=telegram.ParseMode.HTML)
    else:
        print("message is empty...........................................")


def send_mina(msg):

    message=msg
    if(message!=''):
        time.sleep(2) # Sleep for 3 seconds
        status = bot.send_message(chat_id='@mina_tradingofficials', text=message, parse_mode=telegram.ParseMode.HTML)
    else:
        print("message is empty...........................................")


