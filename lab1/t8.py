"""
8.Write a Python program that prompts the user to enter a sentence 
and prints out the sentence in all uppercase letters.
"""


def upperCase():
    value = input("Enter a string: ")
    return value.upper()


print(upperCase())