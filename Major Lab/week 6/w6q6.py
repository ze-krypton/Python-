print("Find the area of a triangle and its type")

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Sides must be greater than zero.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("The sum of any two sides must be greater than the third side.")
else:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("Area of triangle:", area)

    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
