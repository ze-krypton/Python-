import math

def Euler(n):
    if n<=0:
        return False
    count=0
    for i in range(1,n+1):
        if math.gcd(n,i)==1:
            count+=1
    return count

print(Euler(int(input("Enter a number: "))))