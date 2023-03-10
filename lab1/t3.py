"""
3.Write a Python function that takes a list of integers as input and 
returns the largest number in the list
"""


def largestNumber(listOfInt):
    return max(listOfInt)

def largestNumber2(listOfInt):
    result = 0
    for elm in listOfInt:
        if elm > result:
            result = elm
    return result
    
test1 = largestNumber([5,2,3,4,5])
test2 = largestNumber2([9,1,5,99,8,2])

print(test1 == 5,"   ",test2 == 99)