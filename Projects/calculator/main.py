
def calculator():
    '''Imports logo if there exist a logo or prints "calculator program!" '''
    try:
        from art import logo
    except:
        logo = "Calculator Program! "
        
    print(logo)
    print("operations: \'+\'   \'-\'   \'/\'  \'*\'")
    op=input("Enter the operation: ")
    if op not in {"+", "-", "*", "/"}:
        print("Enter a valid OP!")
        exit()

    a=int(input("1st number: "))
    should_continue=True
    while should_continue:
        b=int(input("2nd number: "))

        def calc(a,b,op):
            if op=="+":
                return a+b
            elif op=="-":
                return a-b
            elif op=="*":
                return a*b
            elif op=="/":
                return a/b
            else:
                return f"Enter a valid operation!"
        result=calc(a=a,b=b,op=op)
        print(f"{a} {op} {b} = {result}")
        choice=input("Enter \'Y\' to continue with same result and \'n\' to start a new calc: ").lower()
        if choice=="y":
            a=result
        else:
            should_continue=False
            print("\n"*100)
            calculator()
        
calculator()
        

