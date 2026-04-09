import pandas as pd

df = pd.DataFrame({
    "Name": ["Aman","Riya","John","Sara","Raj","Priya"],
    "Age": [25,None,30,22,None,28],
    "Salary": [50000,60000,None,45000,52000,51000],
    "City": ["Delhi","Mumbai",None,"Chennai","Delhi",None]
})

df.columns = ["Name","Age","Salary","City"]

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])

df = df.dropna()

df = df[(df.Age < 50) & (df.Salary >= 50000)]

df = df[["Name","Age","Salary","City"]]

print(df)