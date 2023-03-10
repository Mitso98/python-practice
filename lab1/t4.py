"""
4.Write a Python program that prompts the user to enter their age 
and prints out a message saying whether they are old enough to 
vote (age 18 and above) or not.
"""

def prompter():
    age = input("Enter your age: ")

    try:
        age = int(age)
    except:
        print("Invalid input")
        return "Invalid input"


    if age >= 18:
        print("You have the Right to vote.")
        return True
    
    print("You don't have the right to vote.")
    return False

prompter()


