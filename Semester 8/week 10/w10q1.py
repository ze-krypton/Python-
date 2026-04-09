import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = [12, 18, 25, 22, 30, 28, 35, 40, 38, 45]

plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.bar(x, y)
plt.title("Bar Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.scatter(x, y, color='red', marker='o')
plt.title("Scatter Plot")


