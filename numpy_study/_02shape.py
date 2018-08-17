# -*- coding: utf-8 -*-
import numpy as np
a = np.arange(1,3)
print(a,a.shape,sep="\n")
print('test_a----------end')
b = np.array([[1,2,3,4],[4,5,6,7]])
print(b,b.shape,sep="\n")
print('test_b----------end')
c = np.array([[np.arange(1,5),
			   np.arange(5,9),
	           np.arange(9,13)],
	          [np.arange(13,17),
	           np.arange(17,21),
	           np.arange(21,25)]])
print(c,c.shape,type(c),sep="\n")
print(a.dtype)
print('test_c----------end')
d = np.array(['A','B','C','DEF'])
print(d.dtype)
print(d)
e = d.reshape(2,2)#更改为2维
print(d)
print('test_d----------end')
print(e)
f = a.astype(str)#更改属性
print(a.dtype)#更改后本身属性不变 返回值属性改变
print(f.dtype)
print(f)
for i in range(c.shape[0]):
	for j in range(c.shape[1]):
		for k in range(c.shape[2]):
			print(c[i][j][k],c[i,j,k])
print('test_f----------end')
print(c[0])
print("------")
print(c[0,0])
print("---------")
print(c[0,0,0])
