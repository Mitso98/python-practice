"""
Question 13:
Create a subclass Circle that inherits from Shape and has an attribute radius. 
Implement a method in each subclass that returns the area
of the shape.
"""
import math


class Shape:
    def __init__(self, radius) -> None:
        self.radius = radius


class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__(radius)

    def area(self) -> float:
        return self.radius**2 * math.pi


circle = Circle(5)
print(circle.area())
