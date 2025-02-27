def compute_average(numbers):
    if len(numbers) != 5:
        raise ValueError("Please provide exactly five numbers.")
    return sum(numbers) / len(numbers)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

# Example usage
numbers = [10, 20, 30, 40, 50]
average = compute_average(numbers)
print(f"Average: {average}")

celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")

length = 10
width = 5
perimeter = perimeter_of_rectangle(length, width)
print(f"Perimeter of the rectangle: {perimeter}")
