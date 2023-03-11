"""
    8 - Write a Python program that reads a file named example.txt and
writes its contents to a new file named copy. txt.
    """

with open("example.txt", "r") as f:
    file = f.read()
    
with open("example_copy.txt", "w") as f:
    f.write(file)