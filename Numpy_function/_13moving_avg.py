# -*- coding: utf-8 -*-
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd
dates, closing_prices = np.loadtxt(
    'data/aapl.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    dtype=np.dtype('M8[D], f8'),
    converters={1: dmy2ymd})
ma51 = np.zeros(closing_prices.size - 4)
# 五日平均价
for i in range(ma51.size):
    ma51[i] = closing_prices[i:i + 5].mean()
# np.ones(5) 产生五个1数组,做有效卷积
ma52 = np.convolve(closing_prices,
                   np.ones(5) / 5, 'valid')
# 取指数曲线的五个点
weights = np.exp(np.linspace(-1, 0, 5))
print('1:',weights)
weights /= weights.sum()
print('2:',weights)
# 注意这儿的weights[::-1],使卷积计算时离的越近权重越大
ma53 = np.convolve(closing_prices,
                   weights[::-1], 'valid')
print('ma53',ma53)
# 十日均线
ma10 = np.convolve(closing_prices,
                   np.ones(10) / 10, 'valid')
mp.figure('Moving Average', facecolor='lightgray')
mp.title('Moving Average', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(
    md.DayLocator())
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, c='lightgray',
        label='Closing Price')
mp.plot(dates[4:], ma51, c='orangered',
        linewidth=1, label='MA-51')
mp.plot(dates[4:], ma52, c='orangered',
        alpha=0.25, linewidth=5, label='MA-52')
mp.plot(dates[4:], ma53, c='limegreen',
        label='MA-53')
mp.plot(dates[9:], ma10, c='dodgerblue',
        label='MA-10')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
