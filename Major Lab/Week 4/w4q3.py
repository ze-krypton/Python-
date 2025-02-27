print("Write a Python function which accepts the radius of a circle from the user and computes the area.\n")


def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = (22/7)* (radius ** 2)
    print(f"The area of the circle with radius {radius} is {area:.2f}")

# Example usage
area_of_circle()
