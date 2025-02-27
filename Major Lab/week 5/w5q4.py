print("Write a Python program to count the occurrences of each word in a given sentence.")

def count_word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Example usage
sentence = "this is a test. This is only a test."
print(count_word_occurrences(sentence.lower()))
