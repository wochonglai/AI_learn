
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as mp


x = np.linspace(-np.pi, np.pi, 1000)
cos_y = np.cos(x)/2
sin_y = np.sin(x)
mp.figure('Sin',figsize=(6,4),dpi=120,facecolor='dodgerblue')
mp.title('Sin',fontsize = 20)
mp.xlabel('x',fontsize=14)
mp.ylabel('y=sin(x)',fontsize=14)
mp.tick_params(labelsize=10)
# 网格线
mp.grid(linestyle=':')

mp.figure('Cos',figsize=(6,4),dpi=120,facecolor='limegreen')
mp.title('Cos',fontsize=20)
mp.xlabel('x',fontsize=14)
mp.ylabel('y=cos(x)',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 将前面的窗口设置为当前的
mp.figure('Cos')
mp.plot(x, cos_y, label=r'$y=\frac{1}{2}cos(x)$')
mp.legend()
mp.figure('Sin')
mp.plot(x, sin_y, label=r'$y=sin(x)$')
mp.legend()
# mp.show()阻塞函数
mp.show()
