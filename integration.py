import pandas as pd

df = pd.read_excel('C:/Users/e.almaee/Desktop/Dataset/Heart data.xlsx')

#df1 = df[[0,1,2,3]]
#df2 = df[[4,5,6,7,8,9,10,11,12,13]]

#df_join = pd.concat([df1, df2])


df_new = df.append(df)

print(len(df), len(df_new))