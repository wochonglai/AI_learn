# -*- coding: utf-8 -*-
'''
梅尔频率倒谱系数
'''
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf # 基于python的语音特征
import matplotlib.pyplot as mp
sample_rate, sigs = wf.read(
    '../data2/speeches/training/pineapple/pineapple01.wav')
mfcc = sf.mfcc(sigs, sample_rate)
mp.matshow(mfcc, cmap='gist_rainbow', fignum='MFCC')
mp.title('MFCC', fontsize=20)
mp.xlabel('Feature', fontsize=14)
mp.ylabel('Sample', fontsize=14)
mp.tick_params(which='both', top=False, labeltop=False,
               labelbottom=True, labelsize=10)
mp.savefig('../data2/pineapple01.png')
mp.show()
