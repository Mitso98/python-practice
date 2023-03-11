"""
6 - Write a Python program that reads a file named example.txt and
prints the contents of the file in reverse order.
    """
    
with open("example.txt", "r") as f:
    file = f.read()

print(file[::-1])



