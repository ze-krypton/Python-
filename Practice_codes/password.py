import string
import random

nr_letter=int(input("Enter the number of letters in Password: "))
nr_digit=int(input("Enter the number of digits in Password: "))
nr_char=int(input("Enter the number of Character in Password: "))

password=[]

for i in range(nr_letter):
    password.append(random.choice(string.ascii_letters))

for i in range(nr_digit):
    password.append(random.choice(string.digits))
    
for i in range(nr_char):
    password.append(random.choice(string.punctuation))
    
random.shuffle(password)
pw=''.join(password)
print("Your Password",pw)
    