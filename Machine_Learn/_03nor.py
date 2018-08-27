# -*- coding: utf-8 -*-
'''
归一化
'''
import numpy as np
import sklearn.preprocessing as sp


raw_samples = np.array([
    [3, -1.5,  2,   -5.4],
    [0,  4,   -0.3,  2.1],
    [1,  3.3, -1.9, -4.3]])
print(raw_samples)
nor_samples = raw_samples.copy()
for row in nor_samples:
    row_absum = abs(row).sum()
    row /= row_absum
print(nor_samples)
nor_samples = sp.normalize(raw_samples, norm='l1')
print(nor_samples)
