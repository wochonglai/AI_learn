import sklearn.datasets as sd
import sklearn.decomposition as dc
import matplotlib.pyplot as mp
faces = sd.fetch_olivetti_faces('../../data/')
x = faces.data
y = faces.target
mp.figure('Explained Variance Ratio',
	facecolor='black')
mp.subplots_adjust(left=0.04, bottom=0.04,
	right=0.96, top=0.96, wspace=0, hspace=0)
rows, cols = 11, 40
