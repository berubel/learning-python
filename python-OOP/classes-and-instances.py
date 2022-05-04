# Python Object-Oriented Programming

# Basics of classes and instances 
# Classes are used when we need to represent unique elements but with the same characterists
# Class are like blueprints and Instances are the unique elements created by the class
# variables -> attributes
# functions -> methods

 # obs: if u want to leavy a class or a function empty for the time being then u can put 'pass' statement
 # obs: all method automatically takes the instance as the first argument 'self'

from cgi import print_arguments
from distutils.command.build_scripts import first_line_re


class Employee():

    def __init__(self, first, last, pay):
        #Attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    def fullname(self): # in this case all arguments that we need is the instance
        return '{} {}'. format(self.first, self.last)

# Instances -> they have different locations in memory because they are different elements
emp_1 = Employee('Gabriele', 'Virgens', 5000) 
emp_2= Employee('Test', 'User', 6000)

print("\n")
print(emp_1)
print(emp_2)

print("\n")
print(emp_1.email)
print(emp_2.email)
print("\n")

# print('{} {}'. format(emp_1.first, emp_1.last))

# Calling the method
print(emp_1.fullname()) # self is puted automatically


# Calling the method by the class
Employee.fullname(emp_1) # the object/instance emp_1 = self, we need to pass it as an argument

'''
Without using attributes declarated in the initializer

emp_1.first = 'Corey'
emp_1.last = 'Turner'
emp_1.email = 'Corey.Turner@company.com'
emp_1.pay = 5000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 6000

print(emp_1.email)
print(emp_2.email)


'''
