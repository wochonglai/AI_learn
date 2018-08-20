# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as mp


n = 1000
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
z =np.sqrt(x**2+y**2)
mp.figure('Scatter',facecolor='lightgray')
mp.title('Scatter',fontsize = 20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# cmap 颜色映射 jet与jet_r渐变色
mp.scatter(x, y, s=60, c=z, cmap='jet', alpha=0.5,
           marker='o')
# 横纵相等
mp.axis('equal')
mp.show()

