# -*- coding: utf-8 -*-
'''
边缘识别
'''
import cv2 as cv
original = cv.imread('../data2/chair.jpg')
cv.imshow('Original', original)
canny = cv.Canny(original, 50, 240)
'''
第2个参数和第3个参数表示阈值，这二个阈值中当中的小阈值用来控制边缘连接，
大的阈值用来控制强边缘的初始分割即如果一个像素的梯度大与上限值，则被认为是边缘像素，
如果小于下限阈值，则被抛弃。如果该点的梯度在两者之间则当这个点与高于上限值的像素点连接时我们才保留，否则删除。??
'''
cv.imshow('Canny', canny)
cv.waitKey()
