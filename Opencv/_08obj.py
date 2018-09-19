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


def search_objects(directory):
    directory = os.path.normpath(directory)
    if not os.path.isdir(directory):
        raise IOError("The directory '" + directory +
                      "' doesn't exist!")
    objects = {}
    for curdir, subdirs, files in os.walk(directory):
        for jpeg in (file for file in files
                     if file.endswith('.jpg')):
            path = os.path.join(curdir, jpeg)
            label = path.split(os.path.sep)[-2]
            if label not in objects:
                objects[label] = []
            objects[label].append(path)
    return objects
