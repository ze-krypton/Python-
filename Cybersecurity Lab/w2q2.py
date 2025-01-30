import math

def compute_gcd(a, b):
    return math.gcd(a, b)


a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print(f"GCD of {a} and {b} is {compute_gcd(a, b)}")
