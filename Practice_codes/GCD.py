a=int(input('Enter a number: '))
b=int(input('Enter 2nd number: '))
def gcd(a,b):
    while b: #while b: means “continue looping as long as b is not zero or False”.
        a,b=b,a%b
    return a 

print(gcd(a,b))