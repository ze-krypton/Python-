# Python Program to Find the Second Largest Number in a List.
print("Python Program to Find the Second Largest Number in a List.")

def second_largest(numbers):
    numbers.sort()
    return numbers[-2]

numbers = [int(x) for x in input("Enter the list of numbers: ").split()]
print(f"Second largest number is {second_largest(numbers)}.")
