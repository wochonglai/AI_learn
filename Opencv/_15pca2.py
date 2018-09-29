import numpy as np
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.decomposition as dc
# 原始样本
A = np.mat(
	'3 2000; 2 3000; 4 5000; 5 8000; 1 2000',
	dtype=float)
print('A =', A, sep='\n')
