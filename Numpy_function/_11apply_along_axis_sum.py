# -*- coding: utf-8 -*-
import datetime as dt
import numpy as np


def dmy2wday(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    wday = date.weekday()
    return wday
wdays, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt(
        'data/aapl.csv', delimiter=',',
        usecols=(1, 3, 4, 5, 6), unpack=True,
        converters={1: dmy2wday})
wdays = wdays[:16]
print('wdays:',wdays)
opening_prices = opening_prices[:16]
highest_prices = highest_prices[:16]
lowest_prices = lowest_prices[:16]
closing_prices = closing_prices[:16]
first_monday = np.where(wdays == 0)[0][0]
print('f_m:',first_monday)
last_friday = np.where(wdays == 4)[0][-1]
print('l_f:',last_friday)
indices = np.arange(first_monday, last_friday + 1)
print('indices:',indices)
indices = np.split(indices, 3)
print('indices:',indices)


def week_summary(indices):
    opening_price = opening_prices[indices[0]]
    highest_price = np.max(np.take(
        highest_prices, indices))
    lowest_price = np.min(np.take(
        lowest_prices, indices))
    closing_price = closing_prices[indices[-1]]
    return opening_price, highest_price, \
        lowest_price, closing_price
summaries = np.apply_along_axis(
    week_summary, 1, indices)
print(summaries)
np.savetxt('data/summary.csv',
           summaries, delimiter=',', fmt='%g')  # %g紧凑浮点格式
