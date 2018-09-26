# -*- coding: utf-8 -*-
'''
 局部二值模式直方图人脸识别
'''
import os
import numpy as np
import cv2 as cv
import sklearn.preprocessing as sp
fd = cv.CascadeClassifier('../data2/haar/face.xml')


def search_faces(directory):
    directory = os.path.normpath(directory)
    if not os.path.isdir(directory):
        raise IOError("The directory '" + directory +
                      "' doesn't exist!")
    faces = {}
    for curdir, subdirs, files in os.walk(directory):
        for jpeg in (file for file in files
                     if file.endswith('.jpg')):
            path = os.path.join(curdir, jpeg)
            label = path.split(os.path.sep)[-2]
            if label not in faces:
                faces[label] = []
            faces[label].append(path)
    return faces

 
train_faces = search_faces('../data2/faces/training')
codec = sp.LabelEncoder()
codec.fit(list(train_faces.keys()))
train_x, train_y = [], []
for label, filenames in train_faces.items():
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faces = fd.detectMultiScale(
            gray, 1.1, 2, minSize=(100, 200))
        for l, t, w, h in faces:
            train_x.append(gray[t:t + h, l:l + w])
            train_y.append(int(
                codec.transform([label])[0]))
train_y = np.array(train_y)

