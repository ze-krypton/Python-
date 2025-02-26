num=int(input("Enter a number: "))

            
def is_prime(n):
    if n<=1:
        print("it is not prime")
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                print(f"{n} is not a prime\nfactor:{i}")
                return
        print(f"{n} is a prime numebr")
is_prime(n=num)
            