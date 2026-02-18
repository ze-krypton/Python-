import numpy as np

arr=np.arange(0,10)
print("Original array: ",arr)

#different MAtrix size

arr_1=arr.reshape(5,2)
print(arr_1)

arr_2=arr.reshape(2,5)
print(arr_2)
