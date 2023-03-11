"""
16 - Write a function that takes a string as input and an arbitrary
number of keyword arguments using **kwargs. The function should
replace all instances of the keyword argument keys in the input
string with their corresponding values.    
    """
    
def func(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
        
func(name="Mostafa", age=24)