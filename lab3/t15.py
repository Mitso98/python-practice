"""
Question 15:
[Polymorphism] Create a class Animal with an abstract method
speak(). Implement subclasses Dog and Cat that override speak() to
output the respective animal sounds.
"""
from abc import abstractmethod


class Animal:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def speak(self) -> None:
        pass


class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()

    def speak(self):
        print("Dog is speaking")

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()

    def speak(self):
        print("Cat is speaking")

cat = Cat()
dog = Dog()

cat.speak()
dog.speak()