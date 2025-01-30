import math

def euler_totient(n):
    count = 0
    for i in range(1, n + 1):
        if math.gcd(n, i) == 1:
            count += 1
    return count


num = int(input("Enter a number: "))
print(f"Euler Totient of {num} is {euler_totient(num)}")
