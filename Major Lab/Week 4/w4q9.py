print("Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters. (Use isupper(), islower(), upper(), lower() functions).")

def count_case_letters(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

# Example usage
input_string = "Hello World!"
upper_count, lower_count = count_case_letters(input_string)
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
