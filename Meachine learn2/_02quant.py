# -*- coding: utf-8 -*-
'''
图像量化
'''
import numpy as np
import scipy.misc as sm
import sklearn.cluster as sc
import matplotlib.pyplot as mp


image = sm.imread('data/lily.jpg',True).astype(np.uint8)  #读取图像,True只保留亮度通道,黑白的
x = image.reshape(-1, 1)
model = sc.KMeans(n_clusters=2)
model.fit(x)
y = model.labels_ # 取到训练时与x对应的聚类点,0类别
centers = model.cluster_centers_.squeeze()  # 去掉多余的维度
print(centers)
z = centers[y]  #用聚类中心点替换其他分类点
print(z.size)
quant = z.reshape(image.shape)

mp.figure('Original Image', facecolor='lightgray')
mp.title('Original Image', fontsize=20)
mp.axis('off')
mp.imshow(image, cmap='gray')

mp.figure('Quant Image', facecolor='lightgray')
mp.title('Quant Image', fontsize=20)
mp.axis('off')
mp.imshow(quant, cmap='gray')
mp.show()
