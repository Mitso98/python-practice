"""
    Question 3:
Create a class Employee with three attributes name, age, and salary.
The class should have a method raise_salary() that increases the
employee's salary by a given percentage.
    """
    
class Employee:
    def __init__(self,name,age,salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        
    def raise_salary(self,percentage) -> None:
        self.salary *= (1 + percentage)

emp = Employee("Mostafa",24,5000)
print(emp.salary)  
emp.raise_salary(1)
print(emp.salary)  
