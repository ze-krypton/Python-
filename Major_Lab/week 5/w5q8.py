print("Write a Python program to reverse words in a string.")

def reverse_words_in_string(s):
    words = s.split()
    return ' '.join(words[::-1])

# Example usage
print(reverse_words_in_string("Hello World!"))
