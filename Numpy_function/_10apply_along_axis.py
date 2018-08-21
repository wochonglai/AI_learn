# -*- coding: utf-8 -*-
'''
np.apply_along_axis(函数, 轴向, 高维数组)
在高维数组中，沿着指定轴向，提起低维子数组，作为参数传递给特定的函数，并将其返回值按照同样的轴向组成成新的数组返回给调用者。
轴向：
二维，0-行方向，1-列方向
三维，0-页方向，1-行方向，2-列方向
'''
import numpy as np


def pingfang(x):
    print('pingfang:', x)
    return x * x
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
Y = np.apply_along_axis(pingfang, 1, X) # 第二个参数,1代表横轴,0代表纵轴
print(Y)
