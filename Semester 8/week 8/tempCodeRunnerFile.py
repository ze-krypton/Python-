
df = pd.read_csv("your_data.csv")

print(df.isnull().sum())                

print((df.isnull().sum()/len(df))*100)
