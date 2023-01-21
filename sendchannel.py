import telegram
import time

bot = telegram.Bot(token='5135949153:AAFr8IZwDOGtCxIX1by6_VGrkFm-3d62tuY')

def send_ramin(msg):

    message=msg
    if(message!=''):
        time.sleep(2) # Sleep for 3 seconds
        status = bot.send_message(chat_id='@ramin_tradingofficials', text=message, parse_mode=telegram.ParseMode.HTML)
    else:
        print("message is empty...........................................")
