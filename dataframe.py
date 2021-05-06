import pandas as pd
import numpy as np

d = {'age': [22, 33, 22, 21, 34, 45], 'gender': ['F', 'M', 'M', 'M', 'F' , 'F']}
df = pd.DataFrame(data=d)

print(df.head(3))
