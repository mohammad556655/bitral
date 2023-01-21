from re import S
import asyncio
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from pandas_datareader import data
from kucoin.client import Client
import cufflinks as cf
from datetime import datetime
import time
from kucoin.asyncio import KucoinSocketManager


client = Client("628a2ce9f39c9b000139b5cf", "04e61232-4199-490f-b097-2453665abdbe", "Ms..556655@")
start = time.mktime(datetime.strptime("2022/07/01", "%Y/%m/%d").timetuple())
end = time.mktime(datetime.strptime("2022/05/31", "%Y/%m/%d").timetuple())


# async def get_data(pair):
    
#     await ksm.subscribe('/market/ticker:ETH-USDT')
    
#     candles = client.get_kline_data(symbol=pair,kline_type='4hour',start=int(start))
    

#     ohlc = pd.DataFrame(candles)
#     ohlc.rename(columns={0: 'date', 1: 'open',2:'close',3:'high',4:'low',5:'volume',6:'amount'}, inplace=True)
#     print(pair+" is analysing ")


#     ohlc['date'] = ohlc['date'].astype(int)

#     for x in range(0 , ohlc.shape[0]):
#       ohlc.date[x] = datetime.fromtimestamp(ohlc.date[x]).strftime('%Y-%m-%d %H:%M:%S')

#     ohlc=ohlc.sort_values(by=["date"], ascending=True)
#     ohlc=ohlc.set_index('date')
#     ohlc=ohlc.astype(float)
#     return ohlc

# get_data("eth")

async def main():
    global loop

    # callback function that receives messages from the socket
    async def handle_evt(msg):
        if msg['topic'] == '/market/ticker:ETH-USDT':
            print(f'got ETH-USDT tick:{msg["data"]}')

        elif msg['topic'] == '/market/snapshot:BTC':
            print(f'got BTC market snapshot:{msg["data"]}')

        elif msg['topic'] == '/market/snapshot:KCS-BTC':
            print(f'got KCS-BTC symbol snapshot:{msg["data"]}')

        elif msg['topic'] == '/market/ticker:all':
            print(f'got all market snapshot:{msg["data"]}')

        elif msg['topic'] == '/account/balance':
            print(f'got account balance:{msg["data"]}')

        elif msg['topic'] == '/market/level2:KCS-BTC':
            print(f'got L2 msg:{msg["data"]}')

        elif msg['topic'] == '/market/match:BTC-USDT':
            print(f'got market match msg:{msg["data"]}')

        elif msg['topic'] == '/market/level3:BTC-USDT':
            if msg['subject'] == 'trade.l3received':
                if msg['data']['type'] == 'activated':
                    # must be logged into see these messages
                    print(f"L3 your order activated: {msg['data']}")
                else:
                    print(f"L3 order received:{msg['data']}")
            elif msg['subject'] == 'trade.l3open':
                print(f"L3 order open: {msg['data']}")
            elif msg['subject'] == 'trade.l3done':
                print(f"L3 order done: {msg['data']}")
            elif msg['subject'] == 'trade.l3match':
                print(f"L3 order matched: {msg['data']}")
            elif msg['subject'] == 'trade.l3change':
                print(f"L3 order changed: {msg['data']}")

    client = Client("628a2ce9f39c9b000139b5cf", "04e61232-4199-490f-b097-2453665abdbe", "Ms..556655@")

    ksm = await KucoinSocketManager.create(loop, client, handle_evt)

    # for private topics such as '/account/balance' pass private=True
    ksm_private = await KucoinSocketManager.create(loop, client, handle_evt, private=True)

    # Note: try these one at a time, if all are on you will see a lot of output

    # Market Execution Data
    await ksm.subscribe('/market/match:BTC-USDT')
    # Level 3 market data
    await ksm.subscribe('/market/level3:BTC-USDT')

    while True:
        print("sleeping to keep loop open")
        await asyncio.sleep(20, loop=loop)


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
