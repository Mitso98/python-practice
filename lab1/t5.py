"""
5.Write a Python function that takes a list of strings as input and 
returns the string with the most characters.
"""

def mostOccurance(stringArray):
    length = 0
    resultIndex = 0
    for index in range(0,len(stringArray)):
        if len(stringArray[index]) > length:
            length = len(stringArray[index])
            resultIndex = index

    return stringArray[resultIndex]

print(mostOccurance(["Asd","qwee","eee"]))