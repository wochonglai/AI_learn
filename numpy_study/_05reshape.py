# -*- coding: utf-8 -*-
# 变维
import numpy as np
a = np.arange(1,9)
b = a.reshape(2,4)
print(b)
c = b.reshape(2,2,2)
print('c:',c)
d = c.ravel() #共享a
print('d:',d)
e = c.flatten() # 复制了另一个a
print('e:',e)
a += 10
#这儿注意  flatten复制了一份,其他都是用的视图方法
print(a,b,c,d,e,sep = '\n')
'''
[11 12 13 14 15 16 17 18]
[[11 12 13 14]
 [15 16 17 18]]
[[[11 12]
  [13 14]]

 [[15 16]
  [17 18]]]
[11 12 13 14 15 16 17 18]
[1 2 3 4 5 6 7 8]
'''
print(a.resize(4,2)) #none
print('a:',a)
f = a.transpose() ##转置f与a共享
print('f1:',f)
f-=10
print('f2:',f)
