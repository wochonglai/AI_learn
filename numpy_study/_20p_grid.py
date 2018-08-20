# -*- coding: utf-8 -*-
'''
坐标系
grid(which=’majar/minor’,axis=’x/y/both 缺省值both’,linwidth=线宽,linestyle=线型’:’点线等等,color)
'''
import numpy as np
import matplotlib.pyplot as mp


n = 1000
x, y = np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
mp.figure('Grid',facecolor='lightgray')
mp.title('Grid',fontsize=20)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.xlim(0,10)
mp.ylim(0,10)
ax=mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(1.0))
ax.yaxis.set_minor_locator(mp.MultipleLocator(0.1))

mp.tick_params(labelsize=10)
mp.grid(which='major',axis='both',linestyle='-',linewidth='0.75',color='lightgray')
mp.grid(which='minor',axis='both',linestyle='-',linewidth='0.25',color='lightgray')
mp.show()
