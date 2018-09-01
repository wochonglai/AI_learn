# -*- coding: utf-8 -*-
import functools


def f1(x):
    return x + 3

def f2(x):
    return x * 6

def f3(x):
    return x - 9

def function_composer(*fs):
    return functools.reduce(lambda fa, fb: lambda x: fa(fb(x)), fs)

a = 1
print('a: ',a)

# (a+3)x6-9
b = f3(f2(f1(a)))
print('b: ',b)

c = functools.reduce(lambda fa, fb: lambda x: fa(fb(x)), [f3, f2, f1])(a)
print('c: ',c)

d = function_composer(f3, f2, f1)(a)
print('d: ',d)
