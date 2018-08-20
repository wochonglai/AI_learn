# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as mp


mp.figure('Subplot',facecolor='lightgray')
mp.subplot(2,2,1) #或者mp.subplot(221)
mp.xticks(())
mp.yticks(())
mp.subplot(224)
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '4', ha='center', va='center',
                size=36, alpha=0.5) #文本:ha水平方向位置,va垂直位置,alpha 透明度
mp.tight_layout() #紧凑布局
mp.show()
