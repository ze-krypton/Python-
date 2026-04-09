import pandas as pd
import numpy as np

data = {
    "Name": ["Aman", "Riya", "John", "Sara", "Raj", "Priya"],
    "Age": [25, None, 30, 22, None, 28],
    "Salary": [50000, 60000, None, 45000, 52000, None],
    "City": ["Delhi", "Mumbai", None, "Chennai", "Delhi", None]
}

df = pd.DataFrame(data)
print(df)

df.rename(columns={
    "Name": "Employee_Name",
    "Age": "Employee_Age",
    "Salary": "Employee_Salary",
    "City": "Employee_City"
}, inplace=True)

print(df)