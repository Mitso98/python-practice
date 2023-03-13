"""
Question 14:
[Encapsulation] Create a class BankAccount with a private attribute
balance. Implement methods deposit and withdraw to modify the
balance, and a method get_balance to retrieve the balance.
"""


class BankAccount:
    def __init__(self, balance) -> None:
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount
    
    def get_balance(self) -> float:
        return self.__balance
        

bank = BankAccount(100)
print(bank.get_balance())
bank.withdraw(10)
print(bank.get_balance())
bank.deposit(10)
print(bank.get_balance())