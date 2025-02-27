print("Write a function to add arbitrary integers.")

def add_arbitrary_integers(*args):
    return sum(args)

# Example usage
print("Sum:", add_arbitrary_integers(1, 2, 3, 4, 5))
