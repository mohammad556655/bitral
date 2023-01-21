import pandas as pd
import talib as tl
def analyze(data, l1=20, offset=0):
    pl = []
    lr = []
    for i in range(len(data)):
        pl.append(data.low[i])
        if(len(pl) >= l1):
            sum_x = 0.0; sum_y = 0.0; sum_xy = 0.0; sum_xx = 0.0; sum_yy = 0.0
            for a in range(1,  len(pl)+1):
                sum_x += a
                sum_y += pl[a-1]
                sum_xy += (pl[a-1] * a)
                sum_xx += (a*a)
                sum_yy += (pl[a-1] * pl[a-1])
            m = ((sum_xy - sum_x * sum_y / l1) / (sum_xx - sum_x * sum_x / l1))
            b = sum_y / l1 - m * sum_x / l1
            if(offset==0):
                lr.append(b + m * l1)
            else:
                lr.append(b+ m * (l1-offset))
            pl = pl[1:]
    lr_pd = pd.DataFrame(lr)
    lr_pd.rename(columns={0:'lsma'}, inplace=True)
    # if(offset!=0):
    #     for i in range(1,len(lr_pd)):
    #         lr_pd.lsma[i] = lr_pd.lsma[i]*(l1-1-offset)
    return lr_pd