# -*- coding: utf-8 -*-
'''
.视频捕捉
'''
import numpy as np
import cv2 as cv
vc = cv.VideoCapture(0)  # 0 - 视频捕捉设备编号
while True:
    frame = vc.read()[1]
    cv.imshow('VideoCapture', frame)
    if cv.waitKey(33) == 27:  # 30 fps,延时33ms,一秒内30幅画面,按键返回
        break
vc.release()    # vc资源释放
cv.destroyAllWindows()  # 高版本opencv可不调用
