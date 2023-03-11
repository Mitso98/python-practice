"""
7 - Write a Python program that reads a file named example.txt and
removes all newline characters from the file.
"""

with open("example.txt", "r") as f:
    file = f.read().replace("\n", "")

print(file)