# Python Program to Merge Two Lists and Sort it.
print("Python Program to Merge Two Lists and Sort it.")

list1 = [int(x) for x in input("Enter the first list of numbers: ").split()]
list2 = [int(x) for x in input("Enter the second list of numbers: ").split()]
merged_list = sorted(list1 + list2)
print("Merged and sorted list:", merged_list)
