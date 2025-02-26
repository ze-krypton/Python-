def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

sentence = input("Enter a sentence: ")
counts = count_words(sentence)

print("\nWord occurrences:")
for word in counts:
    print(f"{word}: {counts[word]}")