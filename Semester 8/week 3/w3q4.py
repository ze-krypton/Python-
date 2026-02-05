sentence = input("Enter a sentence: ")
count =sum(1 for ch in sentence.lower() if ch in "aeiou")
print(count)   
