"""
Question 11:
[Multilevel inheritance] Create a class Person with an attribute
name. Create a subclass Employee that inherits from Person and has
an attribute salary. Create a subclass Manager that inherits from
Employee and has an attribute department. Implement a method in
Manager that returns the name, salary, and department of the
manager.
"""


class Person:
    def __init__(self, name) -> None:
        self.name = name


class Employee(Person):
    def __init__(self, name, salary) -> None:
        super().__init__(name)
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department) -> None:
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print(
            f"Name: {self.name}, Salary: {self.salary}, Dep: {self.department}")

manager = Manager("Mostafa", 5000, "IT")

manager.display()