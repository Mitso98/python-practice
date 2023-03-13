"""
    Question 2:
Create a class Circle with one attribute radius. The class should have
a method circumference() that returns the circumference of the
circle.
    """

import math


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def circumference(self) -> float:
        return 2 * math.pi * self.radius
    
circle = Circle(5)
print(circle.circumference())
