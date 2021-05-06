import pandas as pd
import numpy as np

df = pd.read_excel('C:/Users/e.almaee/Desktop/Dataset/Heart data.xlsx')

print(df.head())

print(df.isnull().sum())

#df = df.dropna(how='all')
df = df.dropna(thresh=11)
df['ca'] = df['ca'].fillna(1)
df['thal'] = df['thal'].fillna(method='bfill')
df = df.dropna(subset=['cholestoral '])
df['slope'] = df['slope'].fillna(df['slope'].mean())

print(df.isnull().sum())










