# -*- coding: utf-8 -*-
'''
热成像图
在矩阵格子里填充不同颜色而成
mp.imshow(矩阵, cmap=颜色映射,
                      origin=垂直轴方向)
'''
import numpy as np
import matplotlib.pyplot as mp


n = 1000
x, y =np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
z = (1-x/2+x**5 + y**3)*np.exp(-x**2-y**2)
mp.figure('Hot',facecolor='lightgray')
mp.title('Hot',fontsize=20)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.imshow(z,cmap='jet',origin='low')
mp.show()
