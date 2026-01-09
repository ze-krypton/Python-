print("Write a Python program which accepts the inputs from the user and does the following using functions:")

import math

def largest_of_three(a, b, c):
    return max(a, b, c)

def volume_of_cylinder(radius, height):
    return math.pi * (radius ** 2) * height

def volume_of_cube(side):
    return side ** 3

def volume_of_rectangular_box(length, width, height):
    return length * width * height

def area_of_rectangle(length, width):
    return length * width

def circumference_of_circle(radius):
    return 2 * math.pi * radius

def exchange_values(a, b):
    return b, a

def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Example usage
a, b, c = 10, 20, 30
print(f"Largest of {a}, {b}, {c}: {largest_of_three(a, b, c)}")

radius, height = 5, 10
print(f"Volume of cylinder with radius {radius} and height {height}: {volume_of_cylinder(radius, height)}")

side = 4
print(f"Volume of cube with side {side}: {volume_of_cube(side)}")

length, width, height = 2, 3, 4
print(f"Volume of rectangular box with length {length}, width {width}, and height {height}: {volume_of_rectangular_box(length, width, height)}")

length, width = 5, 6
print(f"Area of rectangle with length {length} and width {width}: {area_of_rectangle(length, width)}")

radius = 7
print(f"Circumference of circle with radius {radius}: {circumference_of_circle(radius)}")

a, b = 100, 200
a, b = exchange_values(a, b)
print(f"After exchange, a: {a}, b: {b}")

x1, y1, x2, y2 = 0, 0, 3, 4
print(f"Distance between points ({x1}, {y1}) and ({x2}, {y2}): {distance_between_points(x1, y1, x2, y2)}")
