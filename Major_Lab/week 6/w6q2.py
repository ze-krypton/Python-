print("Find the smallest of three numbers")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a <= b and a <= c:
    print("Smallest number:", a)
else:
    print("Smallest number:", min(b, c))
