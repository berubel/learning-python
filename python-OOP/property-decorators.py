# Prperty Decorators - Gtters, Setters and Deleters
'''These allow us to give our class attributes, getter, setter and deleter functionality
We define a method but we can acess it like an attribute'''

from posixpath import split


class Employee():

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self): 
        return '{} {}'. format(self.first, self.last)
    @property
    # It's a method but we're able to acess it like an attribute (no parenteses), that's a getter method
    def email(self): 
        return '{}{}@email.com'. format(self.first, self.last)
    # Creating a setter method. The decorator is the name-of-method.setter. After that create a method with the same name as the method you want to create a setter.
    @fullname.setter
    def fullname(self, name): #the name is what we waant to set
        first, last = name.split(' ') #the first part splited will be the first name and the second part after the space will be the last name
        self.first = first
        self.last = last

    # Creating a deleter method, which going to be similar to the setter method
    @fullname.deleter
    def fullname(self): #the name is what we waant to set
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Gabriele', 'Virgens') 

# If we change the first attribute only, the email being an attribute still has our old first name
emp_1.first = 'Eloise'

# Using the setter method we can change the attributes (self.) by the method that allow us to set new values for them
emp_1.fullname = ('Gabriele Virgens')

print("\n")
print(emp_1.first)
# Using the email as a method the problem is solved. 
# But that will be better if you acess the email function like an attribute not a method. 
# To do this just add a property decorator above the method
print(emp_1.email)
# print(emp_1.email)
print(emp_1.fullname)

# To use the deleter method put 'del' at the beginning of the line
del emp_1.fullname