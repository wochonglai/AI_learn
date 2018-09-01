# -*- coding: utf-8 -*-
import functools


def f1(x, y):
    print('f1:', x, y)
    return x + y

a = [3, 4, 5]
print(a)
b = sum(a)
print(b)
#c = functools.reduce(f1, a)
c = functools.reduce(lambda x, y: x + y, a)
print(c)
