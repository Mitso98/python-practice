"""
11 - Write a function that takes a list of strings as input and returns a
new list containing only the strings that start with the letter "a".    
    """
    
def onlyA(listOfStr):
    result = []
    for word in listOfStr:
        if word.startswith("a"):
            result.append(word)
    return result

print(onlyA(["a","b","qwe","asd"]))
        