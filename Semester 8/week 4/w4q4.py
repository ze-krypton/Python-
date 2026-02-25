number =input('Enter numbers seprated by spcae: ')

number_list=list(map(int,number.split()))

ascending = sorted(number_list)
descending = sorted(number_list, reverse=True)

print("Ascending Order:", ascending)
print("Descending Order:", descending)

