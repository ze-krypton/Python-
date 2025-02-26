def octal(n):
    if n==0:
        return "0"
    elif n==1:
        return str(n)
    else:
        return octal(n//16)+str(n%16)

print(octal(int(input("Enter "))))

decimal_number = 456
hex_number = hex(decimal_number)  # Converts to hexadecimal
print(hex_number)  # Output: 0x1c8