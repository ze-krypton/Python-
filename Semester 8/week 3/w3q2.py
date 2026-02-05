num1 = int(input("Enter 1 number: "))
num2 = int(input("Enter 2 number: "))
num3 = int(input("Enter 3 number: "))

if num1 > num2 and num1 > num3:
    print("1st is greatest")

elif num2 > num1 and num2 > num3:
    print("2nd is greatest")

elif num3 > num1 and num3 > num2:
    print("3rd is greatest")

elif num1 == num2 and num1 > num3:
    print("1st and 2nd are greatest")

elif num2 == num3 and num2 > num1:
    print("2nd and 3rd are greatest")

elif num1 == num3 and num1 > num2:
    print("1st and 3rd are greatest")

else:
    print("All are equal")
