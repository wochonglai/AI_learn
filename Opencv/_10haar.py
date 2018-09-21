# -*- coding: utf-8 -*-
'''
基于哈尔级联分类器的人脸定位
'''
import numpy as np
import cv2 as cv
fd = cv.CascadeClassifier('../data2/haar/face.xml')
ed = cv.CascadeClassifier('../data2/haar/eye.xml')
nd = cv.CascadeClassifier('../data2/haar/nose.xml')
vc = cv.VideoCapture(0)  # 0 - 视频捕捉设备编号
while True:
    frame = vc.read()[1]
    faces = fd.detectMultiScale(frame, 1.3, 5)  # 多尺度检测,1.3代表脸部的最小范围,5最多找多少张脸
    for l, t, w, h in faces:
        a, b = int(w / 2), int(h / 2)   #椭圆水平半径与垂直半径
        cv.ellipse(frame, (l + a, t + b), (a, b), 0,
                   0, 360, (255, 0, 255), 2)    # (l + a, t + b) 圆心坐标
        face = frame[t:t + h, l:l + w]  # 只看脸所在图像处,切片
        eyes = ed.detectMultiScale(face, 1.3, 5)    # face注意坐标系
        for l, t, w, h in eyes:
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(face, (l + a, t + b), (a, b), 0,
                       0, 360, (0, 255, 0), 2)
        noses = nd.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in noses:
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(face, (l + a, t + b), (a, b), 0,
                       0, 360, (255, 0, 0), 2)
    cv.imshow('VideoCapture', frame)
    if cv.waitKey(33) == 27:  # 30 fps
        break
vc.release()
cv.destroyAllWindows()
