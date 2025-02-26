import math

n=int(input("Enter a number: "))

def is_perfct(num):
    if n<=0:
        return False
    sum_of_divisors=sum(i for i in range(1,n)if n%i==0)
    return sum_of_divisors==n

if is_perfct(n):
    print(f"{n} is a Perfect no.")
else:
    print(f"{n} is NOt a Perfect no.")