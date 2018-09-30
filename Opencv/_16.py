import sklearn.datasets as sd
import sklearn.decomposition as dc
import matplotlib.pyplot as mp
faces = sd.fetch_olivetti_faces('../../data/')
x = faces.data
y = faces.target
ncps = range(10, 410, 10)
evrs = []
