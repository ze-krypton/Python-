# Write a program in Python to check a number for Armstrong. (while)
print("Write a program in Python to check a number for Armstrong. (while)")

def is_armstrong(number):
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return number == sum

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
