"""
Question 16:
Create a class Calculator with a class method add that takes two
numbers as arguments and returns their sum.
"""


class Calculator:
    def __init__(self) -> None:
        pass

    def add(self, num1, num2):
        return num1 + num2


calc = Calculator()
print(calc.add(5, 5))
