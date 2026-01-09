# Python Program to Find the Second Largest Number in a List Using Bubble Sort.
print("Python Program to Find the Second Largest Number in a List Using Bubble Sort.")

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def second_largest_bubble_sort(numbers):
    sorted_numbers = bubble_sort(numbers)
    return sorted_numbers[-2]

numbers = [int(x) for x in input("Enter the list of numbers: ").split()]
print(f"Second largest number is {second_largest_bubble_sort(numbers)}.")
