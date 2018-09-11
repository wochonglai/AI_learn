# -*- coding: utf-8 -*-
'''
opencv-python基础使用,蓝绿红通道提取,缩放
'''
import numpy as np
import cv2 as cv
original = cv.imread('../data2/forest.jpg')
print(original.shape)
cv.imshow('Original', original)
# 创建与original维度一样的o矩阵
blue = np.zeros_like(original)
