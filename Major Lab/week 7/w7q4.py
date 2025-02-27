# Write a program in Python to compute factorial of an integer n recursively. (function)
print("Write a program in Python to compute factorial of an integer n recursively. (function)")

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial_recursive(number)}.")
