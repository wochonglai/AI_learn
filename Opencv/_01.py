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
gray = cv.cvtColor(original,cv.COLOR_BAYER_BG2GRAY)
print(gray.shape)
cv.imshow('Gray', gray)

h, w = original.shape[:2]
l, t = int(w / 4), int(h / 4)
r, b = int(w * 3 / 4), int(h * 3 / 4)
cropped = original[t:b, l:r]
cv.imshow('Cropped', cropped)
'''
scaled = cv.resize(original, (w * 2, int(h / 2)),
                   interpolation=cv.INTER_LINEAR) # 压缩
'''
scaled = cv.resize(original, None, fx=2, fy=0.5,
                   interpolation=cv.INTER_LINEAR) #线性插值,扩展
cv.imshow('Scaled', scaled)
cv.waitKey()
cv.imwrite('../data2/blue.jpg', blue)
cv.imwrite('../data2/green.jpg', green)
cv.imwrite('../data2/red.jpg', red)
cv.imwrite('../data2/cropped.jpg', cropped)
cv.imwrite('../data2/scaled.jpg', scaled)
