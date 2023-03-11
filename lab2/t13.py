"""
13 - Write a function that takes a list of numbers as input and
returns the largest and smallest numbers in the list.    
    """
def picker(numsList):
    largest = 0
    smallest = 0
    for num in numsList:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

large,small = picker([0,1,2,5,6])
print(large, small)
