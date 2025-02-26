
def is_isntance(lst):
    return sum(item for item in lst if isinstance(item,(int,float)))

sum1=eval(input("Enter a list of numbers and characters: "))
print(f"Sum of numbers: {is_isntance(sum1)}")
