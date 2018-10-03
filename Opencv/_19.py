# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.datasets as sd
import sklearn.decomposition as dc
import matplotlib.pyplot as mp
x, y = sd.make_circles(n_samples=500, factor=0.2,
                       noise=0.04)
model = dc.KernelPCA(kernel='rbf',
                     fit_inverse_transform=True,
                     gamma=10)
kpca_x = model.fit_transform(x)
