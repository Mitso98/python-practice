"""
9.Write a Python function that takes a list of integers as input and 
returns a new list containing only the even numbers.
"""

def onlyEven(listOfInt):
    result = []
    for elm in listOfInt:
        if elm % 2 == 0:
            result.append(elm)
    return result

print(onlyEven([1,2,3,4,5]))