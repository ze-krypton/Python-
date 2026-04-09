import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

df = pd.DataFrame({
    'A': np.random.randint(10, 100, 20),
    'B': np.random.randint(20, 120, 20),
    'C': np.random.randint(5, 80, 20)
})

sns.scatterplot(x='A', y='B', data=df)
plt.title("Scatter Plot")
plt.show()

corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()