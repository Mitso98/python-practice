"""
9 - Write a Python program that reads a file named example.txt and
prints the longest word in the file.
    """


with open("example.txt", "r") as f:
    file = f.read()

prevLength = 0
currentLength = 0
prevWord = ""
currentWord = ""

for char in file:
    if char != "\n":
        currentLength += 1
        currentWord += char
    else:
        if prevLength < currentLength:
            prevLength = currentLength
            prevWord = currentWord

        currentWord = ""
        currentLength = 0

if prevLength < currentLength:
    prevLength = currentLength
    prevWord = currentWord

print(prevWord)
