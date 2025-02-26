def is_range(r1,r2):
    return list(range(r1,r2+1))

r1=int(input("Enter a starting range: "))
r2=int(input("Enter a Ending range: "))

if r1<r2:
    print(f"List : {is_range(r1,r2)}")
else:
    print("Enter starting range smaller than ending range")