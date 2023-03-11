"""
    15 - Write a function that takes an arbitrary number of lists as input
using *args and returns a new list that contains all the elements
from all the input lists.
    """
    
def combine(*args):
    result = []
    for list in args:
        for elm in list:
            result.append(elm)
    return result

print(combine([1,2,3],[5,6,7]))
