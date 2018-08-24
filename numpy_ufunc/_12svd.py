# -*- coding: utf-8 -*-
'''
奇异值分解
'''
import numpy as np


M = np.mat('4 11 14; 8 7 -2')
print(M)
U, s, V = np.linalg.svd(M, full_matrices=False) #full_matrices参数设置是否填充
S = np.diag(s)
print(U, S, V, sep='\n')
print(U * U.T, V * V.T, sep='\n')
print(U * S * V)
