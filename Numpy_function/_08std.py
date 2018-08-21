# -*- coding: utf-8 -*-
import numpy as np


closing_prices = np.loadtxt('data/aapl.csv',delimiter=',',usecols=(6),unpack=True)
mean = np.mean(closing_prices)
devs = closing_prices - mean
pvar = (devs ** 2).mean()
pstd = np.sqrt(pvar)  # 总体方差
print(pstd)
pstd = np.std(closing_prices) # 总体标准差
print(pstd)
svar = (devs ** 2).sum() / (devs.size - 1)#样本方差
sstd = np.sqrt(svar)  #样本标准差
print(sstd)
sstd = np.std(closing_prices, ddof=1)
print(sstd)
