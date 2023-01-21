from ast import keyword
from distutils.command.build_scripts import first_line_re
from operator import truediv
from re import X
from socket import dup
from warnings import catch_warnings
from xmlrpc.client import FastMarshaller
from analyzers import dtoscillator
from test import get_data

import numpy as np
from scipy.signal import argrelextrema
import pandas as pd
import matplotlib.pyplot as plt
from analyzers import rsi
import plotly.graph_objects as go
import time
pair='XTZ-USDT'
timeframe = '30m'
ohlc = get_data(pair=pair,timeframe=timeframe, limit=1500)
ohlc=ohlc.reset_index()

closes = ohlc.close


maxima=argrelextrema(closes.values, np.greater)[0]
maxima_pd = pd.DataFrame(maxima)
maximas=[]
dates_maxima=[]
for tuple in maxima_pd[0]:
    maximas.append(ohlc.close[tuple])
    dates_maxima.append(ohlc.date[tuple])

maximas_pd = pd.DataFrame(maximas)
dates_maxima_pd=pd.DataFrame(dates_maxima)

maximas_pd.rename(columns={0: 'close'}, inplace=True)
dates_maxima_pd.rename(columns={0: 'date'}, inplace=True)
filtered_maxima_close=[]
filtered_maxima_date=[]

resist_close=[]
temp_resist_close=[]
resist_date=[]
def num_sim(n1, n2):
    """ calculates a similarity score between 2 numbers """
    if n1!=0 and n2!=0:
        return 1 - abs(n1 - n2) / (n1 + n2)
    else:
        return -1
def strong(df,i,n):
    if i+n<=df.shape[0]:
        for j in range(i,i+n):
            if df.close[i]<df.close[j]:
                return 0
    if i-n>=0:
        for j in range(i-n,i):
            if df.close[i]<df.close[j]:
                return 0

    return 1

def is_resist(df1,l,n1,n2):
    for i in range(l-n1+1 , l+1):
        if(i>=1 and i< df1.shape[0]):
            if df1.high[i]>df1.high[i-1]:
                return 0
    for i in range(l+1 , l+n2+1):
        if(i>=1 and i< df1.shape[0]):
            if df1.high[i]<df1.high[i-1]:
                return 0

    return 1


def hit(x, y):
    countx = 0
    county = 0

    for i in range(0, maximas_pd.shape[0]):

        maxima = maximas_pd.close[i]
        if (0.9 <= y / x <= 1.1):
            if (0.95 <= maxima / x <= 1.05) and (0.95 <= maxima / y <= 1.05):
                if (abs(maxima - x) > abs(maxima - y)):
                    countx += 1
                elif abs(maxima - y) > abs(maxima - x):
                    county += 1
    return countx, county

def hit_filter():
    for i in range (0 , len(resist_close)-1):
        for j in range (1 , len(resist_close)):
            if(i < len(resist_close) and j < len(resist_close)):
                x = resist_close[i]
                y = resist_close[j]

                # hitx , hity = hit(x,y)
                # if(hitx > hity):
                #     resist_close.pop(j)
                # elif(hitx<hity):
                #     resist_close.pop(i)
                if(x!=y):
                    hitx , hity = hit_by_low(x,y)
                    # print(hit_by_low(x,y))
                    if(hitx > hity):
                        resist_close.pop(j)
                    elif(hitx<hity):
                        resist_close.pop(i)



def hit_by_low(x, y):
    countx = 0
    county = 0
    countx_body = 0
    county_body = 0
    for i in range(0, len(filtered_maxima_close)):

        open = ohlc.open[i]
        close = ohlc.close[i]
        low = ohlc.low[i]
        # if is_resist(ohlc,i,5,2)==1:
        if ohlc.close[i]>ohlc.open[i]:
            if (num_sim(x,y)>=0.99):
                if  num_sim(open,x)>0.995 and num_sim(open,y)>0.995:
                    if (x >= low and x <= open):
                        countx += 1
                    if (y >= low and y <= open):
                        county += 1
            if (countx == county and countx > 0):
                if (x > y):
                    countx -= 1
                elif (y > x):
                    county -= 1


        if (num_sim(x,y)>=0.99):
            if num_sim(close,x)>0.995 and num_sim(close,y)>0.995:
                if (x >= low and x <= close):
                    countx += 1
                if (y >= low and y <= close):
                    county += 1
            if (countx == county and countx > 0):
                if (x > y):
                    countx -= 1
                elif (y > x):
                    county -= 1

    return countx, county

temp_filter=[]


for i in range (1,maximas_pd.shape[0]-1):
    # if(minimas_pd.close[i+5] > minimas_pd.close[i]<minimas_pd.close[i-5]):
        if strong(maximas_pd,i,n=15)==1:

            filtered_maxima_close.append(maximas_pd.close[i])
            filtered_maxima_date.append(dates_maxima_pd.date[i])
# temp_filter_pd= pd.DataFrame(temp_filter)
# temp_filter_pd.rename(columns={0: 'close'}, inplace=True)


# for i in range (1,temp_filter_pd.shape[0]-1):

#     if(temp_filter_pd.close[i+1] > temp_filter_pd.close[i]<temp_filter_pd.close[i-1]):


#         filtered_minima_close.append(temp_filter_pd.close[i])


for i in range(0,len(filtered_maxima_close)-1):
    counter=0
    x = filtered_maxima_close[i]
    for j in range (i,len(filtered_maxima_close)):
        y = filtered_maxima_close[j]
        if num_sim(x,y)>=0.95 and x!=y   :
            # if(x>y and duplicate1==0 and duplicate2==0):
                # for pc in range(0,minimas_pd.shape[0]):
                #     pivot = minimas_pd.close[pc]
                #     if pivot/y<1.05 and pivot/y>1 :
            # index=ohlc[ohlc.close==y].index
            # if is_resist(ohlc,index[0],2,2)==1:
                # print(x)
                # print(y)
                counter= counter+1
    if counter>=1:
        # for z in range(0 , len(resist_close)):
        #     if  resist_close[z]/x<=1.001:
        #         print(x)
        #         print(resist_close[z])
        #         print("\n")
        #     else:
                resist_close.append(x)
                resist_date.append(filtered_maxima_date[j])
                # print(counter)
            # print(x)
            # print(resist_close[z])
            # print("\n")


hit_filter()
thershold = 0.99
print(resist_close)
if timeframe == '4h':
    thershold = 0.97
elif timeframe == '1h':
    thershold = 0.99

for i in range(0 , len(resist_close)):
    for j in range(0 , len(resist_close)):
        x = resist_close[i]
        y = resist_close[j]
        similarity = num_sim(x,y)
        if(similarity>thershold):
            print(similarity)
            if x>y:

                resist_close[i]=0
            elif x<y:
                resist_close[j]=0
resist_close = list(dict.fromkeys(resist_close))
if resist_close.count(0)>0:
    resist_close.remove(0)
# resist_close.append(maximas_pd.close.max())
resist_close_pd = pd.DataFrame(resist_close)
resist_date_pd = pd.DataFrame(resist_date)
resist_close_pd.rename(columns={0: 'close'}, inplace=True)
resist_date_pd.rename(columns={0: 'date'}, inplace=True)
# print(resist_close_pd)
# print(resist_date_pd)
print(resist_close_pd)

resist_close_pd.to_csv('close.csv')
filtered_maxima_close_pd = pd.DataFrame(filtered_maxima_close)
filtered_maxima_date_pd = pd.DataFrame(filtered_maxima_date)
filtered_maxima_close_pd.rename(columns={0: 'close'}, inplace=True)
filtered_maxima_date_pd.rename(columns={0: 'date'}, inplace=True)
filtered_maxima_date_pd = pd.concat([filtered_maxima_date_pd, filtered_maxima_close_pd], axis=1, join='outer')

filtered_maxima_date_pd = filtered_maxima_date_pd.set_index('date')
smooth_prices = filtered_maxima_close_pd.close.rolling(window=5).mean().dropna()

# dates_minima_pd=pd.concat([dates_minima_pd,minimas_pd],axis=1,join='outer')
dates_maxima_pd = pd.concat([dates_maxima_pd, maximas_pd], axis=1, join='outer')

maxima_pd.rename(columns={0: 'num'}, inplace=True)
maxima_counts = maxima_pd.shape[0] - 1

dates_maxima_pd = dates_maxima_pd.set_index('date')
ohlc = ohlc.set_index('date')
plt.plot(ohlc.close)
plt.plot(filtered_maxima_date_pd,'o')
plt.show()
fig = go.Figure(data=[go.Candlestick(x=ohlc.index,
                                     open=ohlc.open
                                     , high=ohlc.high
                                     , low=ohlc.low
                                     , close=ohlc.close)])
for i in range(0, resist_close_pd.shape[0]):
    fig.add_shape(type='line', x0=ohlc.index[0], y0=resist_close_pd.close[i]
                  , x1=ohlc.index[ohlc.shape[0] - 1], y1=resist_close_pd.close[i])

fig.show()

# for i in range(0,len(filtered_minima_close)-1):
#     x = filtered_minima_close[i]
#     count = 0
#     for j in range (i,len(filtered_minima_close)):
#         y = filtered_minima_close[j]
#         duplicate = temp_resist_close.count(y)
#         if(duplicate<=0):
#             if (x/y<=1.005 and x>y)or(x<y and y/x<=1.005) :
#                 count+=1
#             if count>=2:
#                 resist_close.append([x,y])
#                 temp_resist_close.append(x)
#                 temp_resist_close.append(y)
#                 resist_date.append([filtered_minima_date[i],filtered_minima_date[j]])
#                 break

# for i in range(0,minimas_pd.shape[0]-1):
#     counter=0
#     for j in range (0,minimas_pd.shape[0]):
#         x = minimas_pd.close[i]
#         y = minimas_pd.close[j]
#         duplicate1 = resist_close.count(y)
#         duplicate2 = resist_close.count(x)
#         if (x/y<=1.5 and x>y)or(x<y and y/x<=1.5) :
#             if(x>y and duplicate1==0 and duplicate2==0):
#                 for pc in range(0,minimas_pd.shape[0]):
#                     pivot = minimas_pd.close[pc]
#                     if pivot/y<1.005 and pivot/y>1:
#                         index=ohlc[ohlc.close==pivot].index
#                         if is_resist(ohlc,index[0],3,3)==1:
#                             counter= counter+1
#         if counter>2:
#             resist_close.append(y)
#             resist_date.append(dates_minima_pd.date[j])
#             break


# for i in range(0,len(resist_close)-1):
#     for j in range (1,len(resist_close)):
#         x0 = resist_close[i][0]
#         y0 = resist_close[j][0]
#         x1 = resist_close[i][1]
#         y1 = resist_close[j][1]
#         if x0!=0 and x1!=0 and y1!=0 and y0!=0:
#             if (x0>x1 or y0>y1) and (x0/x1<=1.001 or y0>y1<=1.001):

#                 resist_close[j][0]=0
#                 resist_close[j][1]=0
#                 resist_date[j][0]=0
#                 resist_date[j][1]=0

# for i in range(0,len(resist_close)):
#     if(i<len(resist_close)):
#         x = resist_close[i][0]
#         y = resist_close[i][1]
#         if x0==0 or y0==0:
#             resist_close.pop(i)
#             resist_date.pop(i)


# # plt.plot(dates_maxima_pd,'o')
# plt.show()

# # cf.set_config_file(offline = True)
# # qf = cf.QuantFig(ohlc)
# # qf.iplot()

