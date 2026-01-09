import math


num = int(input("Enter a number: "))


expr1 = 5 * num * num + 4
expr2 = 5 * num * num - 4


sqrt_expr1 = int(math.sqrt(expr1))
sqrt_expr2 = int(math.sqrt(expr2))

if sqrt_expr1 * sqrt_expr1 == expr1 or sqrt_expr2 * sqrt_expr2 == expr2:
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is NOT a Fibonacci number.")
