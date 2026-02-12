import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])


print("1D array:", arr1)
print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("Slice 1 to 4:", arr1[1:5])
print("Every other element:", arr1[::2])
print("Reversed array:", arr1[::-1])