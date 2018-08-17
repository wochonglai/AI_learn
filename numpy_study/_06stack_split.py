# -*- coding: utf-8 -*-
import numpy as np

a = np.arange(11,20).reshape(3,3)
b = a +10
print("b:",b)
# 垂直合并
# c = np.vstack((a,b))
# 或者
c = np.concatenate((a,b),axis=0)
print("c:",c)
# 垂直拆分
# d,e,f = np.vsplit(c,3)
# 或者
d,e,f = np.split(c,3,axis=0)
print(d,e,f,sep="\n")
print('---------------')
# 水平合并
# c2 = np.hstack((a,b))
# 或者
c2 = np.concatenate((a,b),axis=1)
print("c2:",c2)
# 垂直拆分
# d2,e2,f2 = np.hsplit(c,3)
# 或者
d2,e2,f2 = np.split(c,3,axis=1)
print(d2,e2,f2,sep="\n")
