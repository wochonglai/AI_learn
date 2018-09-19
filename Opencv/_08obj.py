# -*- coding: utf-8 -*-
'''
图像识别
'''
import os
import warnings
import numpy as np
import cv2 as cv
import hmmlearn.hmm as hl
warnings.filterwarnings('ignore',
                        category=DeprecationWarning)
np.seterr(all='ignore')


train_objects = search_objects(
    '../data2/objects/training')
train_x, train_y = [], []
for label, filenames in train_objects.items():
    descs = np.array([])
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # 取图像的高和宽
        h, w = gray.shape[:2]
        # 放大倍数
        f = 200 / min(h, w)
        gray = cv.resize(gray, None, fx=f, fy=f)
        star = cv.xfeatures2d.StarDetector_create()
        # 取图像的关键点
        keypoints = star.detect(gray)
        sift = cv.xfeatures2d.SIFT_create()
        _, desc = sift.compute(gray, keypoints)
        if len(descs) == 0:
            descs = desc
        else:
            descs = np.append(descs, desc, axis=0)  # axis=0按行扩展
    train_x.append(descs)
    train_y.append(label)
models = {}
for descs, label in zip(train_x, train_y):
    model = hl.GaussianHMM(
        n_components=4, covariance_type='diag',
        n_iter=1000)    #covariance_type='diag'协方差,对角线,n_iter最大迭代次数
    models[label] = model.fit(descs)
test_objects = search_objects(
    '../data2/objects/testing')
test_x, test_y, test_z = [], [], []
