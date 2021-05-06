from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import scale


iris = datasets.load_iris()
X = iris.data
Y = iris.target

Xnorm = MinMaxScaler().fit_transform(X)

print(X)
print(Xnorm)

Xscale = scale(X)
print(Xscale)

