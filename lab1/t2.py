"""
2.Write a Python program that prompts the user to enter two 
numbers and prints out their sum, difference, product, and 
quotient.
"""

def prompter():
    val1 = input("Enter value one: ")
    val2 = input("Enter value two: ")
    
    try:
        sum = int(val1) + int(val2)
        diff = int(val1) - int(val2)
        product = int(val1) * int(val2)
    except:
        print("Invalid input")
        return "Invalid input"

    print("Sum: " , sum )
    print("Differance " , diff)
    print("Product " , product)

prompter()