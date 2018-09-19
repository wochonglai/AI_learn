# -*- coding: utf-8 -*-
'''
特征(描述)矩阵
'''
import cv2 as cv
import matplotlib.pyplot as mp
original = cv.imread('../data2/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
star = cv.xfeatures2d.StarDetector_create()
