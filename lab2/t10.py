"""
10 - Write a function that takes a list of integers as input and returns
the sum of all even numbers in the list.    
    """
    
def sumEven(listOfInt):
    result = 0
    for elm in listOfInt:
        if elm % 2 == 0:
            result += elm
    return result

print(sumEven([1,2,2,1,2]))