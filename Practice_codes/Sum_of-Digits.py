import math

n=int(input("Enter a minimum of 2 didgit num :"))
count=len(str(n))

if count>1:
    sum=0
    for i in str(n):
      sum+=int(i)
    print(f"Sum of digit {n} is : {sum}")  
else:
    print("Enter a number having minimum of 2 digits")