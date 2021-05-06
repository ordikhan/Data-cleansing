import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import random

random.seed(2002)

iris = datasets.load_iris()
X = iris.data
Y = iris.target


KNNmodel = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(KNNmodel, X, Y, cv=10)

print(scores.mean(), scores.std())


pred = cross_val_predict(KNNmodel, X, Y, cv=10)
print(pred)

