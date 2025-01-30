def is_power_of_two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1


num = int(input("Enter a number: "))
if is_power_of_two(num):
    print(f"{num} is in the form of 2^k.")
else:
    print(f"{num} is NOT in the form of 2^k.")
