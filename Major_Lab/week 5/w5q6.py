print("Write a Python program to remove existing indentation from all of the lines in a given text.")

def remove_indentation(text):
    lines = text.split('\n')
    return '\n'.join(line.strip() for line in lines)

# Example usage
text = """
    This is an indented line.
        This is another indented line.
"""
print(remove_indentation(text))
