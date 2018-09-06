# -*- coding: utf-8 -*-
'''
文本分类
'''
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb    #朴素贝叶斯分类器

# 大批量文件加载,指定字符集(默认ASSIC)
train = sd.load_files(
    '../data2/20news', encoding='latin1',
    shuffle=True, random_state=7)
train_data = train.data
# 类别标签
train_y = train.target
print(set(train_y))

# 类别标签代表的语义字符串形式
categories = train.target_names
cv = ft.CountVectorizer()
# 稀疏矩阵
train_bow = cv.fit_transform(train_data)
tt = ft.TfidfTransformer()
train_x = tt.fit_transform(train_bow)
model = nb.MultinomialNB()
model.fit(train_x, train_y)
test_data = [
    'The curveballs of right handed pitchers tend to curve to the left',
    'Caesar cipher is an ancient form of encryption',
    'This two-wheeler is realy good on slippery roads']
test_bow = cv.transform(test_data)
test_x = tt.transform(test_bow)
pred_test_y = model.predict(test_x)
print(pred_test_y)
for sentence, index in zip(test_data, pred_test_y):
    print(sentence, '->', categories[index])
