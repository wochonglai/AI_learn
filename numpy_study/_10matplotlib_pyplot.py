# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-np.pi, np.pi, 1000)
cos_y = np.cos(x)/2
sin_y = np.sin(x)
xo = np.pi*3/4
yo_cos = np.cos(xo)/2
yo_sin = np.sin(xo)
mp.xlim(x.min()*1.1,x.max()*1.1)
mp.ylim(sin_y.min()*1.1,sin_y.max()*1.1)
mp.yticks([-1,-0.5,0.5,1])
mp.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi*3/4,np.pi],
          [r'$-\pi$',r'$-\frac{\pi}{2}$','0',r'$\frac{\pi}{2}$',r'$\frac{3\pi}{4}$',r'$\pi$'])
ax = mp.gca()
ax.spines['left'].set_position(('data','0'))
ax.spines['bottom'].set_position(('data','0'))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

mp.plot(x, cos_y,linestyle ='--',linewidth = 3,color='green',label=r'$y=\frac{1}{2}cos(x)$')
mp.plot(x,sin_y,linestyle =':',linewidth =2,color = 'blue',label=r'y=sin(x)')
# mp.legend(loc='upper left')
mp.plot([xo,xo],[yo_cos,yo_sin],linestyle = '-',color = 'orangered',linewidth =2)
mp.scatter([xo,xo],[yo_cos,yo_sin],s =60,color = 'limegreen',facecolor = 'white',zorder = 3)
mp.annotate(
  r'$\frac{1}{2}cos(\frac{3\pi}{4}=-\frac{\sqrt{2}}{4})$',
  xy=(xo,yo_cos),xycoords ='data',
  xytext =(-90,-40),textcoords = 'offset points',
  fontsize =14,
  arrowprops =dict(arrowstyle ='->',connectionstyle = 'arc3,rad=0.2'))
mp.annotate(
  r'$sin\frac{3\pi}{4}=\frac{\sqrt{2}}{2}$',
  xy=(xo,yo_sin),xycoords ='data',
  xytext =(10,10),textcoords = 'offset points',
  fontsize =14,
  arrowprops =dict(arrowstyle ='->',connectionstyle = 'arc3,rad=0.2'))
mp.legend()
mp.show()
'''
matplotlib.pyplot (mp)
1.	缺省样式
曲线图
mp.plot(水平坐标数组, 垂直坐标数组)
x: [1 2 3 4]
y: [5 6 7 8]
代码：plt1.py
2.线型,线宽和颜色
mp.plot(..., linestyle=线型, linewidth=线宽,
    color=颜色)
代码：plt2.py
3.设置坐标范围
mp.xlim(左边界, 右边界)
mp.ylim(底边界, 顶边界)
代码：plt3.py
4.设置刻度标签
mp.xticks(刻度位置数组, 刻度文本数组)
mp.yticks(刻度位置数组, 刻度文本数组)
代码：plt4.py
5.十字坐标轴
ax = mp.gca() # 当前坐标图
ax.spines[‘’位置’].set_position(坐标系,位置坐标)
ax.spines[‘位置t’].set_color(颜色) # 无色 ‘none’
位置: left,right,bottom,top
6.图例
plot(…,label = 图例文本)
legend(loc = 位置)
7.特殊点
mp.scatter(水平坐标数组,垂直坐标数组,color=’’,zorder = 3,s = 60)
zorder = 3 表示第三层次绘制,s表示点大小
8.备注
annotate(备注文本,目标位置xy,目标坐标系xycoords,备注位置xytext,备注坐标系textcoords,字体大小fontsize,箭头属性arrowprops)

'''
