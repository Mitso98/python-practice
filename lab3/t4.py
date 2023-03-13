"""
Question 4:
Create a class Book with two attributes title and author. The class
should have a method display() that prints the title and author of the
book.
"""


class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def display(self):
        print(f"Book title: {self.title}, Book author: {self.author}.")


book = Book("Fantasy", "Mostafa")
book.display()
