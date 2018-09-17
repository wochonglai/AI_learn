# -*- coding: utf-8 -*-
'''
sift特征检测
'''
import cv2 as cv
original = cv.imread('../data2/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
sift = cv.xfeatures2d.SIFT_create()
