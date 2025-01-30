import math

def are_relatively_prime(a, b):
    return math.gcd(a, b) == 1


a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
if are_relatively_prime(a, b):
    print(f"{a} and {b} are relatively prime.")
else:
    print(f"{a} and {b} are not relatively prime.")
