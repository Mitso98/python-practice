"""
6.Write a Python program that prompts the user to enter a number 
and prints out a message saying whether the number is positive, 
negative, or zero.
"""

def signIndecator():
    value = input("Enter a number: ")

    try:
        value = int(value)
    except:
        return "Enter a valid input"
    
    if value == 0:
        return "zero"
    elif value > 0:
        return "positive"
    
    return "negative"

print(signIndecator())

