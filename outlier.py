import numpy as np

x = np.random.normal(300,10,10000)
x = np.append(x, 90000)

def erase_outliers(data):
    u = np.median(data)
    s = np.std(data)
    filtered = [e for e in data if (u-2*s < e < u+2*s)]
    return filtered


xnew = erase_outliers(x)
print(x.mean())
print(np.mean(xnew))



# multivariate shwartz

from sklearn import datasets
from scipy import stats

iris = datasets.load_iris()
X = iris.data
Y = iris.target

Xnew = X[(np.abs(stats.zscore(X)<2).all(axis=1))]
print(X.shape, Xnew.shape)