input_string = input("Enter a string: ")
if len(input_string) < 2:
    result_string = ""
else:
    result_string = input_string[:2] + input_string[-2:]
print("Result string:", result_string)
