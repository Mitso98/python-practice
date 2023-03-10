"""
7.Write a Python function that takes a string as input and returns the 
number of vowels in the string.
"""

def numberOfVowles(string):
    vowles = {"a":1,"e":1,"i":1,"o":1,"u":1}
    result = 0

    for char in string:
        if vowles.get(char, 0):
            result += 1

    return result

print("Number of vowels is : " , numberOfVowles("adfa"))
print("Number of vowels is : " , numberOfVowles("qwy"))

