print("Write a Python program to remove the characters which have odd index values of a given string.")

def remove_odd_index_characters(s):
    return ''.join([char for index, char in enumerate(s) if index % 2 == 0])

# Example usage
print(remove_odd_index_characters("Hello World!"))
