# -*- coding: utf-8 -*-
'''
决策树
'''
import sklearn.datasets as sd   # 标准数据集,保证数据标准准确
import sklearn.utils as su
import sklearn.tree as st
import sklearn.ensemble as se
import sklearn.metrics as sm    # 性能评估


housing = sd.load_boston()
print(housing.feature_names)
print(housing.data.shape)
print(housing.target.shape)
x, y = su.shuffle(housing.data, housing.target,
                  random_state=7)
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
model = se.AdaBoostRegressor(
    st.DecisionTreeRegressor(max_depth=4),
    n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
for test, pred_test in zip(test_y, pred_test_y):
    print(test, '->', pred_test)
