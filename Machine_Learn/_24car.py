# -*- coding: utf-8 -*-
'''
评估汽车档次,编码与反向编码
'''
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms


data = []
with open('data/car.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
data = np.array(data).T
print('data: ',data)
encoders, train_x = [], []
for row in range(len(data)):
    encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        train_x.append(encoder.fit_transform(
            data[row]))
    else:
        train_y = encoder.fit_transform(
            data[row])
    encoders.append(encoder)
print('encoders: ', encoders)
print('train_x: ', train_x)
train_x = np.array(train_x).T
model = se.RandomForestClassifier(
    max_depth=9, n_estimators=140, random_state=7)
print(ms.cross_val_score(
    model, train_x, train_y, cv=2,
    scoring='f1_weighted').mean())
model.fit(train_x, train_y)
data = [
    ['high', 'med', '5more', '4', 'big', 'low', 'unacc'],
    ['high', 'high', '4', '4', 'med', 'med', 'acc'],
    ['low', 'low', '2', '4', 'small', 'high', 'good'],
    ['low', 'med', '3', '4', 'med', 'high', 'vgood']]
data = np.array(data).T
test_x = []
for row in range(len(data)):
    encoder = encoders[row]
    if row < len(data) - 1:
        test_x.append(encoder.transform(data[row]))
    else:
        test_y = encoder.transform(data[row])
test_x = np.array(test_x).T
pred_test_y = model.predict(test_x)
print(encoders[-1].inverse_transform(pred_test_y))