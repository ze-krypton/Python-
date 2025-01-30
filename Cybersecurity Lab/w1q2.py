def is_perfect(n):
    if n < 1:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

num = int(input("Enter an integer: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
