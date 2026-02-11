students = {
    "Alice": 82,
    "Bob": 68,
    "Charlie": 91,
    "David": 74,
    "Eva": 88
}

print("Students scoring above 75:")
for name, marks in students.items():
    if marks > 75:
        print(name, ":", marks)
    else:
        print(name,":",marks ,"below 75")
