# -*- coding: utf-8 -*-
'''
numpy.convolve(a, b, 'full'/'same'/'valid')
full 完全卷积
same 同维度卷积
valid  有效卷积
'''
import numpy as np


a = np.arange(1, 6)
print('a:', a)
b = np.arange(6, 9)
print('b:', b)
c = np.convolve(a, b, 'full')
print('c ( full):', c)
c = np.convolve(a, b, 'same')
print('c ( same):', c)
c = np.convolve(a, b, 'valid')
print('c (valid):', c)
