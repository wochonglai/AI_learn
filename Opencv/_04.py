# -*- coding: utf-8 -*-
'''
角点检测
'''
import cv2 as cv
original = cv.imread('../data2/box.png')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
corners = cv.cornerHarris(gray, 7, 5, 0.04) # 7,5分别表示水平与垂直方向角点阈值
corners = cv.dilate(corners, None)
mixture = original.copy()
mixture[corners > corners.max() * 0.01] = [0, 0, 255]
cv.imshow('Mixture', mixture)
cv.waitKey()
