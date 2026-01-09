print("Write a Python program to count and display the vowels of a given text.")

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return {vowel: text.count(vowel) for vowel in vowels if vowel in text}

# Example usage
print(count_vowels("Hello World!"))
