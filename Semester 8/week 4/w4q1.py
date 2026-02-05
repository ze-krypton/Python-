numbers=[1,2,3,4,5,6,7]

def my_sum(numbers):
    total = 0
    for items in numbers:
        total+=items
    return total

print("sum: ", my_sum(numbers),"\nAverage :", my_sum(numbers)/len(numbers))