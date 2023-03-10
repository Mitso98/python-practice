"""
10. Write a Python program that reads in a list of strings and prints 
out the strings in alphabetical order.
"""

def orderStrings():
    strings = input("Enter a sentance: ")
    listOfStrings = []
    stringCollector = ""
    for char in strings:
        if char != " ":
            stringCollector += char
        else:
            listOfStrings.append(stringCollector)
            stringCollector = ""
        
    listOfStrings.append(stringCollector)
    listOfStrings.sort()
    return listOfStrings

print(orderStrings())
