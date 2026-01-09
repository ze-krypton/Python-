print("Write a Python function to calculate the sum of digits of a given decimal integer.")

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage
number = 12345
result = sum_of_digits(number)
print(f"The sum of digits of {number} is {result}")
