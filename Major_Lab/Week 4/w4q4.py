print("Write a Python function to calculate the factorial of a number (a non-negative integer).")

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
