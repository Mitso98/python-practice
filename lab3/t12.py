"""
Question 12:
[Hierarchical Inheritance] Create a class Shape with an attribute
color. Create a subclass Rectangle that inherits from Shape and has
attributes width and height. 
"""
class Shape:
    def __init__(self,color) -> None:
        self.color = color

class Rectangle(Shape):
    def __init__(self, color,width,height) -> None:
        super().__init__(color)
        self.width = width
        self.height = height


rec = Rectangle("red",55,50)
