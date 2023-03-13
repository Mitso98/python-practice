"""
Question 1:
Create a class Rectangle with two attributes width and height. The
class should have a method area() that returns the area of the
rectangle.    
    """

class Rec:
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
    def area(self) -> int:
        return self.width * self.height
    
rec = Rec(5,5)
print(rec.area())