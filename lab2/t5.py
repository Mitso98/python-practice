"""
5- Write a Python program that reads a file named example.txt and
counts the number of lines in the file.
    """

with open("example.txt", "r") as f:
    file = f.read().count("\n") + 1

print(file)
