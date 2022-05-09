# Regular methods, class methods and static methods

# Regular methods in a class take the instance (self) as the first argument
# To create a classmethod just put the decorator "@classmethod" to the top then create a regular method.
''' The decorator "@classmethod" will alter the functionality of our method, using it we'll receive tha class as
 our first argument instead of the instance.
 To pass the class like as an argument, it's a common pass a variable called "cls", because class it's a keyword in python
'''
# Static methods don't pass anything automatically, they don't pass the instance or the class. They baheve just
# like regular functions except we include them in our classes because they have some logical connection with the class.
'''To create a static method we're also going to use a decorator, that decorator calls @staticmethod'''

# Importing modules
import datetime

class Employee():

    num_of_emps = 0  
    raise_amount = 1.04 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        Employee.num_of_emps += 1 
       
    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    def apply_raise(self): 
        self.pay = int(self.pay * self.raise_amount) 

    @classmethod
    def set_raise_amount(cls, amount): # We are working with the class instead of the instance
        cls.raise_amount = amount # we're setting that class variable equal to the value passed like an argument

    @classmethod 
    def from_string(cls, emp_str): # alternative constructor to work with strings. By convention is called from_string
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # this line is going to create a new employee object setting the splited values like as attributes

    # Take a date and return wether or not that was a workday. That has a logical connection to our Employee class, but
    # it doesn't actually depend on any specific instance or class variable.

    @staticmethod
    def is_workday(day): # we just pass the argument that we want to work with
        if day.weekday() == 5 or  day.weekday() == 6: # In python has a function that returns a number for each week day. Monday is equal to 0 and it follows the same order as the week
            return False
        return True

emp_1 = Employee('Gabriele', 'Virgens', 5000) 
emp_2= Employee('Test', 'User', 6000)

emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Aisha-Lang-5000'
emp_str_3 = 'Will-Turner-8000'

''' # Split the string when found the caracter passed ie the hyphen '-'
first, last, pay = emp_str_1.split('-')

# Then we can create a new employee passing the splited string and that would run our a init method
new_emp_1 = Employee(first, last, pay) '''

# Creating a new employee with from_string method, it'll parse the string for us, so we don't need to do this anymore
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# Changing the class variable raise amount by the def set_raise_amount
Employee.set_raise_amount(1.05) # automatically accept the class like as first argument
# That def is the same as doing:
# Employee.raise_amount = 1.05

print("\n")
print(Employee.raise_amount) 
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print("\n")

# Using is_workday method 
my_date = datetime.date(2022, 5, 9)
print(Employee.is_workday(my_date))
