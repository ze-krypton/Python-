num = list(map(int, input("enter").split()))
average = sum(num) / len(num) if num else 0
print(average)
