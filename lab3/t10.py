"""
Question 10:
Create a subclass Dog that inherits from both Animal and Pet and
has an attribute breed. Implement a method in Dog that returns the
name, owner, and breed of the dog.
"""
class Animal:
    def __init__(self, name) -> None:
        self.name = name


class Pet():
    def __init__(self, owner) -> None:
        self.owner = owner


class Dog(Animal,Pet):

    def __init__(self, breed,name,owner) -> None:
        self.breed = breed
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
        
    def details(self):
        return {
            "name": self.name,
            "owner": self.owner,
            "breed": self.breed
        }
        
dog = Dog("PetBull", "Thunder","Mostafa")
details = dog.details()
print(details["name"], details["breed"], details["owner"])
    
