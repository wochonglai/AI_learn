# -*- coding: utf-8 -*-
import sklearn.datasets as sd
import sklearn.decomposition as dc
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as mp


faces = sd.fetch_olivetti_faces('../../data/')
x = faces.data
y = faces.target
model = dc.PCA(n_components=140)
pca_x = model.fit_transform(x)
