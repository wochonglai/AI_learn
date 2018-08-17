# -*- coding: utf-8 -*-
import numpy as np
a = np.arange(1,10)
print(a)
print(a[:3])
print(a[3:6])
print(a[6:])
print(a[::-1])
print(a[:-4:-1]) #[9 8 7]
print(a[-4:-7:-1]) #[6 5 4]

# 2页3行4列
b = np.arange(1,25).reshape(2,3,4)
print(b)
print(b[:,0,0])
print(b[0])
print(b[0,1,::2])
print(b[...,1]) #[[ 2  6 10] [14 18 22]] 取每个第一列
print(b[-1,1:,2:])
