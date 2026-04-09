import pandas as pd

df = pd.read_csv('your_data.csv')

print(df.describe())

df_num = df.select_dtypes(include=['number'])

corr = df_num.corr()

Q1 = df_num.quantile(0.25)
Q3 = df_num.quantile(0.75)
IQR = Q3 - Q1

mask = ~((df_num < (Q1 - 1.5*IQR)) | (df_num > (Q3 + 1.5*IQR))).any(axis=1)

df_clean = df[mask]

print(corr)
print(df_clean.head())