import sklearn.datasets as sd
import sklearn.decomposition as dc
import matplotlib.pyplot as mp
faces = sd.fetch_olivetti_faces('../../data/')
x = faces.data
y = faces.target
ncps = range(10, 410, 10)
evrs = []
for ncp in ncps:
	model = dc.PCA(n_components=ncp)
	model.fit_transform(x)
	evr = model.explained_variance_ratio_.sum()
	evrs.append(evr)
