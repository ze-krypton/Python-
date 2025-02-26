def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

def mersenn(p):
    if not is_prime(p):
        return "Enter a prime number"
    
    m=int(2**p)-1
    
    if is_prime(m):
        return f"2^{p}-1= \"{m}\" is Mersenne Prime"
    else:
        return f"2^{p}-1={m} is NOT Mersenne Prime"
    
num=int(input("Enter a num: "))
print(mersenn(num))

    