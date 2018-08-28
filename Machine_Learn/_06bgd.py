# -*- coding: utf-8 -*-
'''
批量梯度下降做线性拟合
'''
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d


train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])
n_epoches = 1000
lrate = 0.01
epoches, losses = [], []
w0, w1 = [1], [1]
for epoch in range(1, n_epoches + 1):
    epoches.append(epoch)
    losses.append(((train_y - (
        w0[-1] + w1[-1] * train_x)) ** 2).sum() / 2)
    print('{:4} w0={:.8f}, w1={:.8f}, loss={:.8f}'.format(
        epoches[-1], w0[-1], w1[-1], losses[-1]))
    d0 = -(train_y - (
        w0[-1] + w1[-1] * train_x)).sum()
    d1 = -((train_y - (
        w0[-1] + w1[-1] * train_x)) * train_x).sum()
    w0.append(w0[-1] - lrate * d0)
    w1.append(w1[-1] - lrate * d1)
w0 = np.array(w0[:-1])
w1 = np.array(w1[:-1])
sorted_indices = train_x.argsort()
test_x = train_x[sorted_indices]
test_y = train_y[sorted_indices]
pred_test_y = w0[-1] + w1[-1] * test_x
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, marker='s', c='dodgerblue',
           alpha=0.5, s=80, label='Training')
mp.scatter(test_x, test_y, marker='D', c='orangered',
           alpha=0.5, s=60, label='Testing')
mp.scatter(test_x, pred_test_y, c='orangered',
           alpha=0.5, s=80, label='Predicted')
for x, y, pred_y in zip(test_x, test_y, pred_test_y):
    mp.plot([x, x], [y, pred_y], c='orangered',
            alpha=0.5, linewidth=1)
mp.plot(test_x, pred_test_y, '--', c='limegreen',
        label='Regression', linewidth=1)
mp.legend()
mp.show()
