import random
import string

password="".join(random.choices(string.digits+string.punctuation+string.ascii_letters,k=8))

print("Your Password: ",password)