"""
12 - Write a function that takes a dictionary as input and returns a
new dictionary with the keys and values swapped (i.e., the keys
become the values and the values become the keys).
"""

def swap(dic):
    result = {}
    for k,v in dic.items():
        result[v] = k
    return result

print(swap({"a":1,"b":2}))