def ispowerof2(n):
    if n<=0:
        return False
    while n%2==0:
        n/=2
    return n==1
num=int(input("enter a number: "))
if ispowerof2(num):
    print(f"{num} is power of 2")
else:
    print(f"{num} is NOT power of 2")