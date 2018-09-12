# -*- coding: utf-8 -*-
'''
star特征检测
'''
import cv2 as cv
original = cv.imread('../data2/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# opencv-contrib-python
star = cv.xfeatures2d.StarDetector_create()
keypoints = star.detect(gray)
mixture = original.copy()
cv.drawKeypoints(original, keypoints, mixture,
                 flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Mixture', mixture)
cv.waitKey()
