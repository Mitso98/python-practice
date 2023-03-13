"""
Question 9:
[Multiple inheritance] Create a class Animal with an attribute name.
Create a class Pet with an attribute owner. 
"""


class Animal:
    def __init__(self, name) -> None:
        self.name = name


class Pet(Animal):
    def __init__(self, owner, name) -> None:
        super().__init__(name)
        self.owner = owner

pet = Pet("Mostafa", "dog")