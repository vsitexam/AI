
import pandas as pd
df=pd.read_csv("D:\\Set\\Important\\Downloads\\Mall_Customers.csv")


import numpy as np


df['Age']=np.where(df['Age']<=60,1,0)
df['SpendingScore']=np.where(df['SpendingScore']>50,1,0)
print(df)

df['count']=1


df=df[['Age','SpendingScore','count']]
df.head()


df=pd.pivot_table(df,
              values='count',
              index=['Age'],
              columns=['SpendingScore'],
              aggfunc=np.size,
              fill_value=0)


print(df)





