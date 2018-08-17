# -*- coding: utf-8 -*-


import numpy as np
a = np.array(['A','B','C'])
b= np.array(['D','E','F'])
c = np.vstack((a,b))
d = np.row_stack((a,b))
print('c:',c)
print('d:',d)
e= np.column_stack((a,b))
f = np.c_[a,b]
print('e:',e)
print('f:',f)
