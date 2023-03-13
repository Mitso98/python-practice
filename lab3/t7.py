"""
Question 7:
Create a class BankAccount with two attributes account_number
and balance. The class should have a constructor that initializes the
account_number and balance attributes. Also, implement a
destructor for the class that prints a message when the object is
destroyed.
"""

class BankAccount:
    def __init__(self,account_number,balance) -> None:
        self.account_number = account_number
        self.balance = balance
        
    def __del__(self):
        print("the object is destroyed.")

bank = BankAccount(55,5000)
  
