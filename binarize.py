import numpy as np
from sklearn.preprocessing import Binarizer

x = np.random.normal(100,12,20)

binobj = Binarizer(threshold=100)
bi = binobj.fit_transform(x)

print(bi)


import pandas as pd
df = pd.read_excel('C:/Users/e.almaee/Desktop/Dataset/Heart data.xlsx')

binobj = Binarizer(threshold=220)
df = df.dropna(subset=['cholestoral '])
bi = binobj.fit(np.asarray(df['cholestoral ']).reshape(-1,1))
df['cholestoral '] = bi.transform(np.asarray(df['cholestoral ']).reshape(-1,1))
