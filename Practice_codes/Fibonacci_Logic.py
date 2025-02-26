import math
n=int(input("Enter the Number: "))

expr1=5*n**2+4
expr2=5*n**2-4

def is_sqrt(n):
    sqrt=math.isqrt(n)
    return sqrt*sqrt==n

if is_sqrt(expr1) or is_sqrt(expr2):
    print(f"{n} is in fibonacci series") 
else:
    print(f"{n} is NOT in fibonacci series") 
