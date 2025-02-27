def consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst) + 1))

numbers = list(map(int, input("Enter the characters and numbers in list: ").split()))

if consecutive(numbers):
    print("The list is consecutive.")
else:
    print("The list is not consecutive.")
