import math

num=int(input("Enter a number: "))
original=num
length=len(num)
add=0
while num!=0:
   rem=num%10
   add+=(rem**length)
   num//=10
   
if original==num:
    print(f"{original} is an armstrong number")
else:
     print(f"{original} is NOT! an armstrong number")
    
    