import pandas as pd

data =[10,20,30]

df =pd.Series(data)
print(df)
data2={
    "Weight" :[58 ,67 ,911],
    "Name" :["Ahmed" ," Aakif","YAsh"]
}

df2=pd.DataFrame(data2, index=[1,2,3])
print(df2.dtypes)
print(df2)