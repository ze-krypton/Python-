print('''Write a program to read the values of two integer variables and exchange the values (Use addition and subtraction operators
A = 5*15 = 5*(16-1) = 5*16 – 5*1 = (5<<<0)''')
a=int(input("Enter a num 1: "))
b=int(input("Enter a num 2: "))
print(f"Before swapping :{a} , {b}")
a=a+b
b=a-b
a=a-b

print(f"After swapping :{a} , {b}")
