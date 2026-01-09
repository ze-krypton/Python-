# Write a program in Python that asks the user how many Fibonacci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. (Without recursion)
print("Write a program in Python that asks the user how many Fibonacci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. (Without recursion)")

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

n_terms = int(input("How many Fibonacci numbers to generate? "))
print("Fibonacci sequence:", fibonacci(n_terms))
