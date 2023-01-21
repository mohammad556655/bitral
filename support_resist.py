import pandas as pd
import numpy as np
import math
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
from get_data import get_data_without_date
import cufflinks as cf

df = get_data_without_date()



#method 1: fractal candlestick pattern
# determine bullish fractal 
def is_support(df,i):  
  cond1 = df['low'][i] < df['low'][i-1]   
  cond2 = df['low'][i] < df['low'][i+1]   
  cond3 = df['low'][i+1] < df['low'][i+2]   
  cond4 = df['low'][i-1] < df['low'][i-2]  
  return (cond1 and cond2 and cond3 and cond4) 
# determine bearish fractal
def is_resistance(df,i):  
  cond1 = df['high'][i] > df['high'][i-1]   
  cond2 = df['high'][i] > df['high'][i+1]   
  cond3 = df['high'][i+1] > df['high'][i+2]   
  cond4 = df['high'][i-1] > df['high'][i-2]  
  return (cond1 and cond2 and cond3 and cond4)
# to make sure the new level area does not exist already
def is_far_from_level(value, levels, df):    
  ave =  np.mean(df['high'] - df['low'])    
  return np.sum([abs(value-level)<ave for _,level in levels])==0
# a list to store resistance and support levels
levels_supp = []
levels_resist = []
for i in range(2, df.shape[0] - 2):  
  if is_support(df, i):    
    low = df['low'][i]    
    if is_far_from_level(low, levels_supp, df):      
      levels_supp.append((i, low))  
  elif is_resistance(df, i):    
    high = df['high'][i]    
    if is_far_from_level(high, levels_resist, df):      
      levels_resist.append((i, high))

cf.set_config_file(offline = True)
ohlc = df.set_index('date')
qf = cf.QuantFig(ohlc)

num_resist = len(levels_resist)
num_supp = len(levels_supp)

list_support=[]
# for x in range(0 , num_supp):
#     list_support.append ( df.loc[levels_supp[x][0]].low)
#     date =df.loc[levels_supp[x][0]].date
#     qf.add_support(date= date,to_strfmt='%Y-%m-%d %H:%M:%S')

for x in range(0 , num_resist):
    list_support.append ( df.loc[levels_resist[x][0]].low)
    date =df.loc[levels_resist[x][0]].date
    qf.add_resistance(date= date,to_strfmt='%Y-%m-%d %H:%M:%S')
qf.iplot(title="btc-usdt")






def plot_all(levels, df):    
  fig, ax = plt.subplots(figsize=(16, 9))   
  candlestick_ohlc(ax,df.values,width=0.6, colorup='green', 
    colordown='red', alpha=0.8)    
  date_format = mpl_dates.dateFormatter('%d %b %Y')
  ax.xaxis.set_major_formatter(date_format)    
  for level in levels:        
    plt.hlines(level[1], xmin = df['date'][level[0]], xmax = 
      max(df['date']), colors='blue', linestyle='--')    
  fig.show()





