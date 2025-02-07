import random
from hangman_words import word_list
from hangman_art import logo,stages

lives=6
print("Welcome to hangman: \"guess the word\" game ", logo)
word_list=["abbas","zooni","zainab"]
chosen_word=random.choice(word_list)
print("_______________________________________________\n")
print("guess the word:" ,chosen_word)

        
placeholder=""
length=len(chosen_word)
for i in range(length):
    placeholder+="_"
print(placeholder)

game_over=False

correct_list=[]

while not game_over:     
    guess=input("Enter a letter: ").lower()
    display=""
    print(f"****************************5{lives}/6 LIVES LEFT****************************")

    if guess in correct_list:
            print(f"You already Guess the letter \"{guess}\" ")
    else:         
        for letter in chosen_word:
            if letter == guess:
                display+=letter
                correct_list.append(letter)
            elif letter in correct_list:
                display+=letter
            else:
                display+="_"
        print(display)

        if guess not in chosen_word:
            lives -= 1
            if lives!=0:
                print(f"You guessed \"{guess}\", that's not in the word. You lose a life")
            else:
                print(f"You guessed \"{guess}\", that's not in the word.")
                game_over= True

                print(f"***********************IT WAS \"{chosen_word.upper()}\"! YOU LOSE**********************")

                    
        if "_" not in display:
            game_over=True 
            print("You win")
    print(stages[lives])