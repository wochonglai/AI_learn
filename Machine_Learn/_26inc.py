# -*- coding: utf-8 -*-
'''

'''
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb


class DigitEncoder():

    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
        return y.astype(int)

    def inverse_transform(self, y):
        return y.astype(str)


num_less, num_more, max_each = 0, 0, 7500
data = []
# 高收入与低收入均只取7500个数
with open('data/adult.txt', 'r') as f:
    for line in f.readlines():
        if '?' not in line:         # 有些数据采集不正确,需要排除
            line_data = line[:-1].split(', ')
            if line_data[-1] == '<=50K' and \
                    num_less < max_each:
                data.append(line_data)
                num_less += 1
            elif line_data[-1] == '>50K' and \
                    num_more < max_each:
                data.append(line_data)
                num_more += 1
            if num_less >= max_each and \
                    num_more >= max_each:
                break
data = np.array(data).T
encoders, x = [], []
for row in range(len(data)):
    if data[row, 0].isdigit():  # 如果是数字特征
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder() #非数字特征做编码转换
    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
    encoders.append(encoder)
x = np.array(x).T
print(x.shape)
train_x, test_x, train_y, test_y = ms.train_test_split(
    x, y, test_size=0.25, random_state=7)
model = nb.GaussianNB()
print(ms.cross_val_score(model, x, y, cv=10,
                         scoring='f1_weighted').mean())
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# 查看预测值与实际的有多少相符合
print((pred_test_y == test_y).sum() / pred_test_y.size)
data = [[
    '39', 'State-gov', '77516', 'Bachelors', '13',
    'Never-married', 'Adm-clerical', 'Not-in-family',
    'White', 'Male', '2174', '0', '40',
    'United-States']]

data = np.array(data).T
'''
底层实现简述:
两个LOAD_FAST:首先把右边b,a对应的引用地址依次放入stack(栈)内,此时该栈顶为[a`,b`];
ROT_TWo:再把栈顶两个地址交换位置,此时栈顶[b`,a`]
两个STORE_FAST:最后,先后从栈顶pop出b`,a`(都是引用地址)存到变量名a,b下
'''
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x)
print(encoders[-1].inverse_transform(pred_y))
