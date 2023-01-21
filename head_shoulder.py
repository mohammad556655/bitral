import pandas as pd
import numpy as np

from datetime import timedelta
import math
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
from test import get_data
from scipy.stats import linregress
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
from scipy.signal import argrelextrema
from collections import defaultdict



def get_max_min(prices, smoothing, window_range):
    smooth_prices = prices['close'].rolling(window=smoothing).mean().dropna()
    local_max = argrelextrema(smooth_prices.values, np.greater)[0]
    local_min = argrelextrema(smooth_prices.values, np.less)[0]
    price_local_max_dt = []
    for i in local_max:
        if (i>window_range) and (i<len(prices)-window_range):
            price_local_max_dt.append(prices.iloc[i-window_range:i+window_range]['close'].idxmax())
    price_local_min_dt = []
    for i in local_min:
        if (i>window_range) and (i<len(prices)-window_range):
            price_local_min_dt.append(prices.iloc[i-window_range:i+window_range]['close'].idxmin())  
    maxima = pd.DataFrame(prices.loc[price_local_max_dt])
    minima = pd.DataFrame(prices.loc[price_local_min_dt])
    max_min = pd.concat([maxima, minima]).sort_index()

    max_min = max_min[~max_min.date.duplicated()]
    p = prices 
    max_min['day_num'] = p[p['date'].isin(max_min.date)].index.values
    max_min = max_min.set_index('day_num')['close']
    
    return max_min

smoothing = 3
window = 10





def find_patterns(max_min):  
    patterns = defaultdict(list)
    
    # Window range is 5 units
    for i in range(5, len(max_min)):  
        window = max_min.iloc[i-5:i]
        
        # Pattern must play out in less than n units
        if window.index[-1] - window.index[0] > 100:      
            continue   
            
        a, b, c, d, e = window.iloc[0:5]
                
        # IHS
        if a<b and c<a and c<e and c<d and e<d and abs(b-d)<=np.mean([b,d])*0.02:
               patterns['IHS'].append((window.index[0], window.index[-1]))
        
    return patterns
pairs=['BTC-USDT','ETH-USDT','ADA-USDT','AXS-USDT','SOL-USDT','IOST-USDT','FLOW-USDT','IOTX-USDT','XMR-USDT','ETC-USDT','XTZ-USDT'
        ,'EGLD-USDT','SAND-USDT','BNB-USDT','ADA-USDT','XRP-USDT','CAKE-USDT','DOGE-USDT','DOT-USDT','AVAX-USDT','MATIC-USDT'
        ,'ALGO-USDT','ICP-USDT','VET-USDT','AAVE-USDT','AXS-USDT','UNI-USDT','FIL-USDT','SHIB-USDT','EOS-USDT','KCS-USDT'
        ,'NEAR-USDT','LTC-USDT','ATOM-USDT','LINK-USDT','BCH-USDT','TRX-USDT','XLM-USDT','MANA-USDT','HBAR-USDT','APE-USDT','FTM-USDT','GRT-USDT'
        ,'THETA-USDT','MKR-USDT']
for pair in pairs:
    df = get_data(pair)
    minmax = get_max_min(df, smoothing, window)
    patterns = find_patterns(minmax)
    print(patterns)

