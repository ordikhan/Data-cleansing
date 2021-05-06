import pandas as pd
import numpy as np

rate = pd.read_csv('C:/Users/e.almaee/Desktop/Dataset/u.data',sep='\t', usecols=[0,1,2]
                    , names=['user_id', 'movie_id', 'rating'])

#print(rate.head())


movie_properties = rate.groupby('movie_id').agg({'rating':[np.size, np.mean]})

print(movie_properties.head())