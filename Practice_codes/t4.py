def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()

    count_1 = 0
    count_2 = 0

    for letter in name1:
        if letter in "true":
            count_1 += 1
        if letter in "love":
            count_1 += 1

    for letter in name2:
        if letter in "true":
            count_2 += 1
        if letter in "love":
            count_2 += 1

    print(f"Your love score: {count_1}{count_2}")

calculate_love_score("Angela Yu", "Jack Bauer")