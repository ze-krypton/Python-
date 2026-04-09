import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("your_data.csv")

numeric_df = df.select_dtypes(include=['number'])

for col in numeric_df.columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# Remove outliers using IQR method
for col in numeric_df.columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]

print("\nData shape after removing outliers:", df.shape)