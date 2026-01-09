d = {"a": 3, "b": 1, "c": 2}

ascending = dict(sorted(d.items(), key=lambda item: item[1]))
descending = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)
