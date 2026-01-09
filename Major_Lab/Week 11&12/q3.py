
from collections import Counter

text=input("Entr a string: ").lower()

letter_counts= Counter(char for char in text if char.isalpha())
print("\nLetter Frequency Histogram:")

for letter , count in sorted(letter_counts.items()):
    print(f"{letter}:{'#' * count}")
