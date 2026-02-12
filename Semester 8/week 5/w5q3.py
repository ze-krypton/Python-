import numpy as np
arr=np.array([i for i in range(1,101)])

primes=[]

for num in arr:
    if num>1:
        is_prime=True
        for i in range(2,int(num**(0.5)+1)):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            primes.append(int(num))
                
                
print(primes)