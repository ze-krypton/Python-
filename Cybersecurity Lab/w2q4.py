def find_narcissistic_numbers(n):
    start = 10**(n-1)
    end = 10**n
    narcissistic_nums = []
    
    for num in range(start, end):
        if sum(int(digit) ** n for digit in str(num)) == num:
            narcissistic_nums.append(num)
    
    return narcissistic_nums


n = int(input("Enter value of 'n': "))
narcissistic_list = find_narcissistic_numbers(n)
print(f"Narcissistic numbers of {n} digits: {narcissistic_list}")
