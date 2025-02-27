# Python Program to Put Even and Odd elements in a List into Two Different Lists.
print("Python Program to Put Even and Odd elements in a List into Two Different Lists.")

def split_even_odd(numbers):
    even_list = []
    odd_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list, odd_list

numbers = [int(x) for x in input("Enter the list of numbers: ").split()]
even_list, odd_list = split_even_odd(numbers)
print("Even elements:", even_list)
print("Odd elements:", odd_list)
