def is_consecutive(lst):
    return sorted(lst)==list(range(min(lst),max(lst)+1))
numbers=list(map(int,input("Enter a list of integers: ").split()))

#   Code	                    Action

# input()	        Gets user input as a string
# .split()	        Splits the string into a list of substrings
# map(int, list)	Converts each substring into an integer ,However, map() does not return a list! It returns a map object (an iterator).
# list(map(...))	Converts the map object into a list

if is_consecutive(numbers):
    print("This list contains Consecutive numbers")
else:
    print("not conseutive")
