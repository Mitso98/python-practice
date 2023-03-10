"""
1.Write a Python function that takes a string as input and returns the string reversed.
"""

def func(string):

    if isinstance(string, str):
        return string[::-1]

    return "Enter a valid input"

print(func("hello world"))
print(func(15))