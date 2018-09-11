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
blue[..., 0] = original[..., 0]  # 0 - 蓝色通道
cv.imshow('Blue', blue)
green = np.zeros_like(original)
green[..., 1] = original[..., 1]  # 1 - 绿色通道
cv.imshow('Green', green)
red = np.zeros_like(original)
red[..., 2] = original[..., 2]  # 2 - 红色通道
cv.imshow('Red', red)
# 灰度转换
