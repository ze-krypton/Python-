num=int(input("Enter a num: "))

count=0
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        count += 1
       
if (count<=2):
    print(f"{num} is Prime number")
else:
    print("not prime")
