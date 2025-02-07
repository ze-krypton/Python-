def calculate_love_score(name1,name2):
    name1=name1.lower()
    name2=name2.lower()
    count_1=0
    count_2=0
    for letters in name1:
        if letters in "true" :
            count_1+=1
        if letters in "love" :
            count_2+=1
    for letters in name2:
        if letters in "true" :
            count_1+=1
        if letters in "love" :
            count_2+=1
    total=print(f"your love Score : {count_1}{count_2}")
    
calculate_love_score("Syed Ahmed Mustafa","Any American Girl")
