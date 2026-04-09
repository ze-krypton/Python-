import pandas as pd
import numpy as np

data = {
    "Name": ["Aman", "Riya", "John", "Sara", "Raj", "Priya"],
    "Age": [25, None, 30, 22, None, 28],
    "Salary": [50000, 60000, None, 45000, 52000, None],
    "City": ["Delhi", "Mumbai", None, "Chennai", "Delhi", None]
}

df = pd.DataFrame(data)

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())          
df["Salary"] = df["Salary"].fillna(df["Salary"].median()) 
df["City"] = df["City"].fillna(df["City"].mode()[0])     

print(df)