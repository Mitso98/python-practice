"""
Question 5:
Create a class Car with four attributes make, model, year, and
mileage. The class should have a method drive() that increments the
mileage of the car by a given amount.
"""

class Car:
    def __init__(self,make,model,year,mileage) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    
    def drive(self,amount) -> None:
        self.mileage += amount

car = Car("Mrecedes", "Beenz", 2022, 50)
print(car.mileage)
car.drive(50)
print(car.mileage)
