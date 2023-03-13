"""
Question 8:
[Single Inheritance] Create a class Vehicle with an attribute speed.
Create a subclass Car that inherits from Vehicle and has an attribute
brand. Implement a method in Car that returns the brand and speed
of the car.
"""


class Vehicle:
    def __init__(self, speed) -> None:
        self.speed = speed


class Car(Vehicle):
    def __init__(self, speed, brand) -> None:
        super().__init__(speed)
        self.brand = brand

    def detalis(self):
        return {
            "brand": self.brand,
            "speed": self.speed
        }
        
car = Car(50,"Toyota")
details = car.detalis()
print("Car brand", details["brand"], "Car speed", details["speed"])
