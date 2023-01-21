import yfinance as yf
import investpy
def get_data(pair = 'EURUSD=X',timeframe = '60m',period = '1d'):
    """
    period: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    
    """
    print(pair+" is analysing")
    data = yf.download(tickers=pair,period=period,interval=timeframe)
    data.index.names=['Date']
    return data















# from alpha_vantage.timeseries import TimeSeries
# import pandas as pd
# def get_data(pair = 'EURUSD',timeframe = '60min',outputsize = 'compact'):
#     """
#     timeframe = '1min', '5min', '15min', '30min', '60min',
#     outputsize = 'compact , 'full'
#     """
#     ts = TimeSeries(key='JQCOBLCVEU9ID060',output_format='pandas',indexing_type='date')
#     data = ts.get_intraday(symbol = pair,interval=timeframe,outputsize=outputsize)
#     d = list(data)
#     # d = pd.DataFrame(data)
#     # print(data)
#     df = pd.DataFrame()
#     df['Open'] = d[0]['1. open']
#     df['High'] = d[0]['2. high']
#     df['Low'] = d[0]['3. low']
#     df['Close'] = d[0]['4. close']
#     df = df.iloc[::-1]
#     return df