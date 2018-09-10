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
