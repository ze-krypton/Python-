A=list(map(int,input("Enter elements for set A: ").split()))
B=list(map(int,input("Enter elements for set B: ").split()))

c=[]

for i in A:
    if i in B:
        c.append(i)

 
print(c)    