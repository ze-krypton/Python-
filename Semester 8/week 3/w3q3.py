n = int (input ("Enter a number :"))
a= 0
b=1
if n==1:
    print(a,b)
elif n==0:
    print(a)
elif n<0:
    print("invalid")
    
else:
    print(a,"\n",b)
    for _ in range (n-2):
        c = a + b
        a , b = b , c
        print(c," ")
    