def is_instance(lst):
    return sum(item for item in lst if isinstance(item,(float,int)))

numbers=list(map(int,input("Enter the charcaters and numbers in list:").split()))

result = is_instance(numbers)

print("Sum of numbers in the list:", result)