import numpy as np

A= np.array([[1,2,3],
             [4,5,6]])
B=np.array([[7,8,9],
            [10 ,11,12]])

print("Matrix A: ")
print(A)

print("Matrix B: ")
print(B)

addition =np.add(A,B)
print("Add:\n ",addition)

mul=np.multiply(A,B)
print("Multiplication:\n ",mul)

#dot_product
B=B.reshape(3,2)
dot_p=np.dot(A,B)
print("Dot prod: ",dot_p)