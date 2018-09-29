import numpy as np
# 原始样本
A = np.mat(
	'3 2000; 2 3000; 4 5000; 5 8000; 1 2000',
	dtype=float)
print('A =', A, sep='\n')
# 归一化缩放：均值为0，极差为1
mu = A.mean(axis=0)
s = A.max(axis=0) - A.min(axis=0)
