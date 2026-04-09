import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=50, scale=15, size=100)

sns.histplot(data, kde=True)
plt.title("Histogram")
plt.show()

sns.boxplot(x=data)
plt.title("Boxplot")
plt.show()