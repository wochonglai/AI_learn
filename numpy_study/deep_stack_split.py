# -*- coding: utf-8 -*-
import numpy as np


a = np.arange(11,20).reshape(3,3)
print('a:',a)
b = a +10
print("b:",b)
# 深度合并
c = np.dstack((a,b))
print('c:',c)
