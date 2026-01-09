print("Write a Python function which accepts the radius of a sphere and computes the volume. What is the volume of a sphere with radius 5?\n")

import math

def volume_of_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

# Example usage
radius = 5
volume = volume_of_sphere(radius)
print(f"The volume of a sphere with radius {radius} is {volume:.2f}")
