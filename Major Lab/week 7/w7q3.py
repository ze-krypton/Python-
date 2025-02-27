# Write a program in Python to generate first n Fibonacci terms recursively. (function)
print("Write a program in Python to generate first n Fibonacci terms recursively. (function)")

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n_terms = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(n_terms):
    print(fibonacci(i), end=" ")
