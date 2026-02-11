number =input('Enter numbers seprated by spcae: ')

number_list=list(map(int,number.split()))

print(sorted(number_list))
