# -*- coding: utf-8 -*-
'''
借助管线连接特征选择器与随机森林分类器
'''
import numpy as np
import sklearn.datasets as sd
import sklearn.feature_selection as fs  #特征选择器
import sklearn.ensemble as se #随机森林
import sklearn.pipeline as pl #管线
import sklearn.model_selection as ms  #模型选择
import matplotlib.pyplot as mp


# 样本生成器
x, y = sd.samples_generator.make_classification(
    n_informative=4, n_features=20, n_redundant=0,
    random_state=5)
print(x.shape,y.shape,np.unique(y))
skb = fs.SelectKBest(fs.f_regression, k=5)  # 特征选择器
rfc = se.RandomForestClassifier(n_estimators=25, max_depth=4)  #随机森林分类器
model = pl.Pipeline([('selector', skb),('classifier', rfc)])
print(ms.cross_val_score(model, x, y, cv=10,
                         scoring='f1_weighted').mean())
model.set_params(selector__k=2,classifier__n_estimators=10) # 修改模型参数
print(ms.cross_val_score(model, x, y, cv=10,scoring='f1_weighted').mean())
model.fit(x, y)
selected_mask = model.named_steps[
    'selector'].get_support()
print(selected_mask)
selected_indices = np.where(selected_mask)[0]
print(selected_indices)
x = x[:, selected_indices]
model.fit(x, y)
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005
grid_x = np.meshgrid(np.arange(l, r, h),
                     np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
mp.figure('Selector-Classifier Pipeline',
          facecolor='lightgray')
mp.title('Selector-Classifier Pipeline', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='Dark2')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='cool', s=60)
mp.show()
