import itertools
import time

def brute_force(target,length):
    digits="0123456789"
    attempts=0

    start_time=time.time()  

    for password_tuple in itertools.product(digits, repeat=length):
        password=''.join(password_tuple)
        attempts+=1

        if password == target_password:
            end_time=time.time()
            print(f"password '{target_password}' cracked! it took {attempts} attempts")
            print(f"time taken : {end_time -start_time:.2f} seconds")
            return password
        
    print(f"Password: '{target_password} not found")
    return None

target_password="43347159"
length=len(target_password)
brute_force(target_password,length)