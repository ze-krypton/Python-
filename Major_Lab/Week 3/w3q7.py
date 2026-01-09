a=int(input("Enter a num a : "))
b=int(input("Enter a num b : "))
print("before:",a, b)

a=a^b
b=a^b
a=a^b

print("After:",a,b)
