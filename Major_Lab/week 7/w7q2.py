# Write a program in Python to print factorial of a number. (for)
print("Write a program in Python to print factorial of a number. (for)")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial(number)}.")
