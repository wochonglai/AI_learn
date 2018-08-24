# -*- coding: utf-8 -*-
import numpy as np


A = np.mat(
    '11 12 13 14; 20 21 22 15; 19 18 17 16')
print(A)
B = np.linalg.pinv(A)
print(B)
C = A * B
print(C)
