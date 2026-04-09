import pandas as pd

file_path = "your_data.csv"   # e.g., data.csv
df = pd.read_csv(file_path)

print("First 5 rows of the dataset:")
print(df.head())

numeric_df = df.select_dtypes(include=['number'])

summary_stats = numeric_df.describe()

print("\nSummary Statistics of Numerical Columns:")
print(summary_stats)

