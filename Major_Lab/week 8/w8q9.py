def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

input_string = input("Enter a long string containing multiple words: ")
reversed_sentence = reverse_words(input_string)
print("Reversed words sentence:", reversed_sentence)
palindrome_check = is_palindrome(input_string)
if palindrome_check:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
