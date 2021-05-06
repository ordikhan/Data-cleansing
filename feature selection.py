import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import random
from sklearn.feature_selection import VarianceThreshold


random.seed(2002)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

#Xnew = VarianceThreshold(0.8 * (1-0.8)).fit_transform(X)

#print(X.shape, Xnew.shape)


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif

Xnew = SelectKBest(chi2, k=2).fit_transform(X,Y)
print(X.shape, Xnew.shape)

Xnew = SelectKBest(f_classif, k=2).fit_transform(X,Y)
print(X.shape, Xnew.shape)

Xnew = SelectPercentile(chi2, percentile=75).fit_transform(X,Y)
print(X.shape, Xnew.shape)



from sklearn.feature_selection import RFE
treemodel = DecisionTreeClassifier()

selector = RFE(treemodel, 3)

Xnew = selector.fit_transform(X,Y)
print(X.shape, Xnew.shape)



