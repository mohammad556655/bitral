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

def find_support(pair , timeframe):
    ohlc = get_data(pair=pair,timeframe=timeframe, limit=120)
    ohlc=ohlc.reset_index()

    Closes = ohlc.Close


    maxima=argrelextrema(Closes.values, np.greater)[0]
    minima=argrelextrema(Closes.values, np.less)[0]
    minima_pd=pd.DataFrame(minima)
    maxima_pd = pd.DataFrame(maxima)
    minimas=[]
    maximas=[]
    Dates_minima=[]
    Dates_maxima=[]
    for tuple in maxima_pd[0]:
        maximas.append(ohlc.Close[tuple])
        Dates_maxima.append(ohlc.Date[tuple])
    for tuple in minima_pd[0]:
        minimas.append(ohlc.Close[tuple])
        Dates_minima.append(ohlc.Date[tuple])
    minimas_pd = pd.DataFrame(minimas)
    maximas_pd = pd.DataFrame(maximas)
    Dates_minima_pd=pd.DataFrame(Dates_minima)
    Dates_maxima_pd=pd.DataFrame(Dates_maxima)

    maximas_pd.rename(columns={0: 'Close'}, inplace=True)
    minimas_pd.rename(columns={0: 'Close'}, inplace=True)
    Dates_maxima_pd.rename(columns={0: 'Date'}, inplace=True)
    Dates_minima_pd.rename(columns={0: 'Date'}, inplace=True)
    filtered_minima_Close=[]
    filtered_minima_Date=[]

    support_Close=[]
    temp_support_Close=[]
    support_Date=[]
    def num_sim(n1, n2):
        """ calculates a similarity score between 2 numbers """
        if n1!=0 and n2!=0:
            return 1 - abs(n1 - n2) / (n1 + n2)
        else:
            return -1
    def strong(df,i,n):
        if i+n<=df.shape[0]:
            for j in range(i,i+n):
                if df.Close[i]>df.Close[j]:
                    return 0
        if i-n>=0:
            for j in range(i-n,i):
                if df.Close[i]>df.Close[j]:
                    return 0

        return 1

    def is_support(df1,l,n1,n2):
        for i in range(l-n1+1 , l+1):
            if(i>=1 and i< df1.shape[0]):
                if df1.Low[i]>df1.Low[i-1]:
                    return 0
        for i in range(l+1 , l+n2+1):
            if(i>=1 and i< df1.shape[0]):
                if df1.Low[i]<df1.Low[i-1]:
                    return 0

        return 1


    def hit(x, y):
        countx = 0
        county = 0

        for i in range(0, minimas_pd.shape[0]):

            minima = minimas_pd.Close[i]
            if (0.9 <= y / x <= 1.1):
                if (0.95 <= minima / x <= 1.05) and (0.95 <= minima / y <= 1.05):
                    if (abs(minima - x) > abs(minima - y)):
                        countx += 1
                    elif abs(minima - y) > abs(minima - x):
                        county += 1
        return countx, county

    def hit_filter():
        for i in range (0 , len(support_Close)-1):
            for j in range (1 , len(support_Close)):
                if(i < len(support_Close) and j < len(support_Close)):
                    x = support_Close[i]
                    y = support_Close[j]

                    # hitx , hity = hit(x,y)
                    # if(hitx > hity):
                    #     support_Close.pop(j)
                    # elif(hitx<hity):
                    #     support_Close.pop(i)
                    if(x!=y):
                        hitx , hity = hit_by_Low(x,y)
                        # print(hit_by_Low(x,y))
                        if(hitx > hity):
                            support_Close.pop(j)
                        elif(hitx<hity):
                            support_Close.pop(i)



    def hit_by_Low(x, y):
        countx = 0
        county = 0
        countx_body = 0
        county_body = 0
        for i in range(0, len(filtered_minima_Close)):

            Open = ohlc.Open[i]
            Close = ohlc.Close[i]
            Low = ohlc.Low[i]
            # if is_support(ohlc,i,5,2)==1:
            if ohlc.Close[i]>ohlc.Open[i]:
                if (num_sim(x,y)>=0.99):
                    if  num_sim(Open,x)>0.995 and num_sim(Open,y)>0.995:
                        if (x >= Low and x <= Open):
                            countx += 1
                        if (y >= Low and y <= Open):
                            county += 1
                if (countx == county and countx > 0):
                    if (x > y):
                        countx -= 1
                    elif (y > x):
                        county -= 1


            if (num_sim(x,y)>=0.99):
                if num_sim(Close,x)>0.995 and num_sim(Close,y)>0.995:
                    if (x >= Low and x <= Close):
                        countx += 1
                    if (y >= Low and y <= Close):
                        county += 1
                if (countx == county and countx > 0):
                    if (x > y):
                        countx -= 1
                    elif (y > x):
                        county -= 1

        return countx, county

    temp_filter=[]


    for i in range (1,minimas_pd.shape[0]-1):
        # if(minimas_pd.Close[i+5] > minimas_pd.Close[i]<minimas_pd.Close[i-5]):
            if strong(minimas_pd,i,n=15)==1:

                filtered_minima_Close.append(minimas_pd.Close[i])
                filtered_minima_Date.append(Dates_minima_pd.Date[i])
    # temp_filter_pd= pd.DataFrame(temp_filter)
    # temp_filter_pd.rename(columns={0: 'Close'}, inplace=True)


    # for i in range (1,temp_filter_pd.shape[0]-1):

    #     if(temp_filter_pd.Close[i+1] > temp_filter_pd.Close[i]<temp_filter_pd.Close[i-1]):


    #         filtered_minima_Close.append(temp_filter_pd.Close[i])


    for i in range(0,len(filtered_minima_Close)-1):
        counter=0
        x = filtered_minima_Close[i]
        for j in range (i,len(filtered_minima_Close)):
            y = filtered_minima_Close[j]
            if num_sim(x,y)>=0.95 and x!=y   :
                # if(x>y and duplicate1==0 and duplicate2==0):
                    # for pc in range(0,minimas_pd.shape[0]):
                    #     pivot = minimas_pd.Close[pc]
                    #     if pivot/y<1.05 and pivot/y>1 :
                # index=ohlc[ohlc.Close==y].index
                # if is_support(ohlc,index[0],2,2)==1:
                    # print(x)
                    # print(y)
                    counter= counter+1
        if counter>=1:
            # for z in range(0 , len(support_Close)):
            #     if  support_Close[z]/x<=1.001:
            #         print(x)
            #         print(support_Close[z])
            #         print("\n")
            #     else:
                    support_Close.append(x)
                    support_Date.append(filtered_minima_Date[j])
                    # print(counter)
                # print(x)
                # print(support_Close[z])
                # print("\n")


    hit_filter()
    thershold = 0.99
    print(support_Close)
    if timeframe == '4h':
        thershold = 0.97
    elif timeframe == '1h':
        thershold = 0.95

    for i in range(0 , len(support_Close)):
        for j in range(0 , len(support_Close)):
            x = support_Close[i]
            y = support_Close[j]
            similarity = num_sim(x,y)
            if(similarity>thershold):
                print(similarity)
                if x>y:

                    support_Close[i]=0
                elif x<y:
                    support_Close[j]=0
    support_Close = list(dict.fromkeys(support_Close))
    if support_Close.count(0)>0:
        support_Close.remove(0)
    support_Close.append(minimas_pd.Close.min())
    support_Close_pd = pd.DataFrame(support_Close)
    support_Date_pd = pd.DataFrame(support_Date)
    support_Close_pd.rename(columns={0: 'Close'}, inplace=True)
    support_Date_pd.rename(columns={0: 'Date'}, inplace=True)
    # print(support_Close_pd)
    # print(support_Date_pd)
    print(support_Close_pd)

    support_Close_pd.to_csv('Close.csv')
    filtered_minima_Close_pd = pd.DataFrame(filtered_minima_Close)
    filtered_minima_Date_pd = pd.DataFrame(filtered_minima_Date)
    filtered_minima_Close_pd.rename(columns={0: 'Close'}, inplace=True)
    filtered_minima_Date_pd.rename(columns={0: 'Date'}, inplace=True)
    filtered_minima_Date_pd = pd.concat([filtered_minima_Date_pd, filtered_minima_Close_pd], axis=1, join='outer')

    filtered_minima_Date_pd = filtered_minima_Date_pd.set_index('Date')
    smooth_prices = filtered_minima_Close_pd.Close.rolling(window=5).mean().dropna()

    # Dates_minima_pd=pd.concat([Dates_minima_pd,minimas_pd],axis=1,join='outer')
    Dates_maxima_pd = pd.concat([Dates_maxima_pd, maximas_pd], axis=1, join='outer')

    minima_pd.rename(columns={0: 'num'}, inplace=True)
    maxima_pd.rename(columns={0: 'num'}, inplace=True)

    minima_counts = minima_pd.shape[0] - 1
    maxima_counts = maxima_pd.shape[0] - 1

    Dates_minima_pd = Dates_minima_pd.set_index('Date')
    Dates_maxima_pd = Dates_maxima_pd.set_index('Date')
    ohlc = ohlc.set_index('Date')
    # plt.plot(ohlc.Close)
    # plt.plot(filtered_minima_Date_pd,'o')
    # plt.show()

    fig = go.Figure(data=[go.Candlestick(x=ohlc.index,
                                         open=ohlc.Open
                                         , high=ohlc.High
                                         , low=ohlc.Low
                                         , close=ohlc.Close)])
    for i in range(0, support_Close_pd.shape[0]):
        fig.add_shape(type='line', x0=ohlc.index[0], y0=support_Close_pd.Close[i]
                      , x1=ohlc.index[ohlc.shape[0] - 1], y1=support_Close_pd.Close[i])

    fig.show()
    # fig.write_image("images\\support.png")

    # for i in range(0,len(filtered_minima_Close)-1):
    #     x = filtered_minima_Close[i]
    #     count = 0
    #     for j in range (i,len(filtered_minima_Close)):
    #         y = filtered_minima_Close[j]
    #         duplicate = temp_support_Close.count(y)
    #         if(duplicate<=0):
    #             if (x/y<=1.005 and x>y)or(x<y and y/x<=1.005) :
    #                 count+=1
    #             if count>=2:
    #                 support_Close.append([x,y])
    #                 temp_support_Close.append(x)
    #                 temp_support_Close.append(y)
    #                 support_Date.append([filtered_minima_Date[i],filtered_minima_Date[j]])
    #                 break

    # for i in range(0,minimas_pd.shape[0]-1):
    #     counter=0
    #     for j in range (0,minimas_pd.shape[0]):
    #         x = minimas_pd.Close[i]
    #         y = minimas_pd.Close[j]
    #         duplicate1 = support_Close.count(y)
    #         duplicate2 = support_Close.count(x)
    #         if (x/y<=1.5 and x>y)or(x<y and y/x<=1.5) :
    #             if(x>y and duplicate1==0 and duplicate2==0):
    #                 for pc in range(0,minimas_pd.shape[0]):
    #                     pivot = minimas_pd.Close[pc]
    #                     if pivot/y<1.005 and pivot/y>1:
    #                         index=ohlc[ohlc.Close==pivot].index
    #                         if is_support(ohlc,index[0],3,3)==1:
    #                             counter= counter+1
    #         if counter>2:
    #             support_Close.append(y)
    #             support_Date.append(Dates_minima_pd.Date[j])
    #             break


    # for i in range(0,len(support_Close)-1):
    #     for j in range (1,len(support_Close)):
    #         x0 = support_Close[i][0]
    #         y0 = support_Close[j][0]
    #         x1 = support_Close[i][1]
    #         y1 = support_Close[j][1]
    #         if x0!=0 and x1!=0 and y1!=0 and y0!=0:
    #             if (x0>x1 or y0>y1) and (x0/x1<=1.001 or y0>y1<=1.001):

    #                 support_Close[j][0]=0
    #                 support_Close[j][1]=0
    #                 support_Date[j][0]=0
    #                 support_Date[j][1]=0

    # for i in range(0,len(support_Close)):
    #     if(i<len(support_Close)):
    #         x = support_Close[i][0]
    #         y = support_Close[i][1]
    #         if x0==0 or y0==0:
    #             support_Close.pop(i)
    #             support_Date.pop(i)


    # # plt.plot(Dates_maxima_pd,'o')
    # plt.show()

    # # cf.set_config_file(offline = True)
    # # qf = cf.QuantFig(ohlc)
    # # qf.iplot()

find_support('BTC-USDT' , '1h')