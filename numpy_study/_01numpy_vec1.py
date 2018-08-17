# -*- coding: utf-8 -*-
import numpy as np
import datetime as dt
n = 100000
starttime = dt.datetime.now()
A,B = [],[]
for i in range(n):
  A.append(i ** 2)
  B.append(i ** 3)
C = []
for a,b in zip(A,B):
  C.append(a+b)
print((dt.datetime.now()-starttime).microseconds)

starttime2 = dt.datetime.now()
A,B = np.arange(n) ** 2,np.arange(n) ** 3
C = A+B
print((dt.datetime.now()-starttime2).microseconds)
