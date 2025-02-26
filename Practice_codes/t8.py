# Write a Python program which accepts the inputs from the user and do the following using functions.
# 	To find largest of 3 numbers using positional arguments.
# 	To find volume of cylinder or cube or rectangular box.
# 	To find area of rectangle.
# 	To find circumference of circle.
# 	To exchange the values of two variables
# 	To find the distance between two points using built-in math method

import math

def greatest(num1,num2,num3):
    if num1>num2 and num1>num2:
        print(f"{num1} is greatest")
    elif num2>num3:
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")

# greatest(num1=int(input("Enter 1st number :")),num2=int(input("Enter 2nd number :")),num3=int(input("Enter 3rd number :")))   

def Volume_cube(s):
    vol=s**3
    return vol

def Volume_Cylinder(r,h):
    vol=math.pi*(r**2)*h
    return vol

def Volume_rectangle(l,b,h):
    vol=l*b*h
    return vol

volume=input("Enter the shape of the desired volume:(cube/cylinder/rectangle) : ").lower()

if volume=="cube":
    print(Volume_cube(int(input("Enter the side of the cube: "))))
elif volume=="rectangle":
    print(Volume_rectangle(int(input("Enter the length :")),int(input("Enter the breadth :")),int(input("Enter the height :"))))
elif volume=="cylinder":
    print(Volume_Cylinder(int(input("Enter the radius :")),int(input("Enter the height :"))))


def exchange(a, b):
    a,b=b,a
    print("Swapped Values: ",a, b)

print(exchange(int(input("Enter 1st number")),int(input("Enter 2nd number"))))

def index(s):
    result=s[::-1]
    print(result)
    
index(input("Enter a String: "))
    

    