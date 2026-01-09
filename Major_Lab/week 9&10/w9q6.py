num = list(map(int, input("Enter elements: ").split()))
x = int(input())

print(f"Found at index {num.index(x)}" if x in num else "Not found")
