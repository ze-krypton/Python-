import pandas as pd

df = pd.read_csv('your_data.csv')
corr = df.corr(numeric_only=True).abs()
upper = corr.where(~(corr < 0.9)).stack().index
drop_cols = set([j for i,j in upper if i!=j])
df = df.drop(columns=list(drop_cols))
print(df.head())