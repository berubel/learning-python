# Special (Magic/Dunder) Methods

'''These special methods allow us to emulate some built-in behaviour in python and it's how 
we implement operator overloading. 
Special methods are preceded by double underscores "__" '''

# double underscores "__" are common called like 'dunder'

class Employee():

    raise_amount = 1.04 

    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"
  
    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    def apply_raise(self): 
        self.pay = int(self.pay * self.raise_amount) 

    # Common special methods

    # repr is met to be an unambiguous representation of the object and should be used for debugging and logging and 
    # things like that. Basically to recreate an object in an easier way
    def __repr__(self) -> str:
        return "Employee('{}','{}', '{}')".format(self.first, self.last, self.pay)
    # str is meant to be more of a readable representation of an object and is meant to be used as a display to the
    # end-user
    def __str__(self) -> str:
        return '{} - {}'.format(self.fullname(), self.email)

    # Add two employees together and the result be their combined salaries
    def __add__(self, other):
        return self.pay + other.pay

    # A function to return the lenght ie the number of caracters in the full name of an employee
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Gabriele', 'Virgens', 5000) 
emp_2= Employee('Test', 'User', 6000)

# The behaviour when we add two strings together is different when we add two integers
# print(1 + 2) # integers are actually added together as a sum
# print('a' + 'b') # Strings are concatenated

print('\n')
''' Initially print a vague employee object, but after we create a special repr method, 
it will print a string result as a reconstruction of the object and once we have created the str method 
it going to print a friendly-user view'''
# print(emp_1) 

# These special methods are going us to get a more user-friendly results
print(repr(emp_1))
print(str(emp_1))
print('\n')

# Do the same thing as the code above
print(emp_1.__repr__())
print(emp_1.__str__())
print('\n')

# There are also many arithmetic special methods

'''When we print a sum, we actually using a dunder method called add, so we can also acess it directly'''
print(1 + 2)
print(int.__add__(1,2))

'''Strings are actually also using your own dunder methods'''
print('a' + 'b')
print(str.__add__('a', 'b'))
print('\n')

# Adding two employees and return their combinated salaries
print(emp_1 + emp_2)
print('\n')

# Another common dunder method is the len method, that returns a lenght of a list
print(len('test'))
# In the background this is what is happening:
print('test'.__len__())
print('\n')

# Using the dunder method len on an employee object to return the employee's full name length
print(len(emp_1))
