# -*- coding: utf-8 -*-
'''
map函数的使用
'''
def f1(x):
    return x + 3


x = 1
y = f1(x)
print(y)

X = [1, 2, 3]
#Y = list(map(f1, X))
Y = list(map(lambda x: x + 3, X))
print(Y)
