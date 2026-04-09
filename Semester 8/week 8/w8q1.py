import pandas as pd

df = pd.read_csv("your_data.csv")

print(df.isnull().sum())
print('\n')                
print((df.isnull().sum()/len(df))*100)

