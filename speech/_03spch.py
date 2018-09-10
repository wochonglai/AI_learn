# -*- coding: utf-8 -*-
'''
隐马尔科夫模型
'''
import os
import warnings
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf
# pip install C:\Users\Python\Downloads\hmmlearn-0.2.1-cp36-cp36m-win_amd64.whl
import hmmlearn.hmm as hl   # 隐马尔科夫模型
warnings.filterwarnings('ignore',
                        category=DeprecationWarning)
np.seterr(all='ignore')


# 该方法查找目录下所有.wav文件,返回对应路径/文件名
def search_speeches(directory, speeches):
    directory = os.path.normpath(directory)
    # 判断目录是否存在
    if not os.path.isdir(directory):
        raise(IOError("The directory '" + directory +
                      "' doesn't exist!"))
    for entry in os.listdir(directory):
