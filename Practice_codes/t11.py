def is_consecutive(lst):
    return sorted(lst)==list(range(min(lst),max(lst)+1))
numbers=list(map(int,input("Enter a series of number seprated by spaces: ").split()))

if is_consecutive(numbers):
    print("It is consecutive number")
else:
    print("It is NOT consecutive number")
    