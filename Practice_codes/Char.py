def Capital(s):
    lower_s=0
    upper_s=0
    
    for char in s:
        if char.isupper():
            upper_s+=1
        elif char.islower():
            lower_s+=1
        
    print(f"no, of lower letters :{lower_s}\nNo, of Capital letters; {upper_s}")

Capital(input("Enter a String: "))        
    
     