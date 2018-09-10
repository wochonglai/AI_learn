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
        label = directory[directory.rfind(os.path.sep) + 1:]
        path = os.path.join(directory, entry)
        # 如果是文件夹
        if os.path.isdir(path):
            search_speeches(path, speeches)
        elif os.path.isfile(path) and \
                path.endswith('.wav'):
            if label not in speeches:
                speeches[label] = []
            speeches[label].append(path)


train_speeches = {}
search_speeches('../data2/speeches/training',
                train_speeches)
train_x, train_y = [], []
for label, filenames in train_speeches.items():
    mfccs = np.array([])
    for filename in filenames:
        sample_rate, sigs = wf.read(filename)
        mfcc = sf.mfcc(sigs, sample_rate)
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            mfccs = np.append(mfccs, mfcc, axis=0)
    train_x.append(mfccs)
    train_y.append(label)
models = {}
for mfccs, label in zip(train_x, train_y):
    model = hl.GaussianHMM(n_components=4,
                           covariance_type='diag',
                           n_iter=1000)
    models[label] = model.fit(mfccs)

# 模型训练完,测试
test_speeches = {}
search_speeches('../data2/speeches/testing',
                test_speeches)
test_x, test_y = [], []
for label, filenames in test_speeches.items():
    mfccs = np.array([])
    for filename in filenames:
        sample_rate, sigs = wf.read(filename)
        mfcc = sf.mfcc(sigs, sample_rate)
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            mfccs = np.append(mfccs, mfcc, axis=0)
    test_x.append(mfccs)
    test_y.append(label)
pred_test_y = []
for mfccs in test_x:
    best_score, best_label = None, None
    for label, model in models.items():
        score = model.score(mfccs)  # 比较相似度得分
        if (best_score is None) or \
           (best_score < score):
            best_score, best_label = score, label
    pred_test_y.append(best_label)
for y, pred_y in zip(test_y, pred_test_y):
    print(y, '->', pred_y)
