dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = dict(dict1.items() | dict2.items())  # Works in Python 3.5+
print(merged)
