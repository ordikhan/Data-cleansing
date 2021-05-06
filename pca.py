import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()

X = iris.data
Y = iris.target

pca = PCA(n_components=2)
pca.fit(X)
Xnew = pca.transform(X)

print(X.shape, Xnew.shape)

