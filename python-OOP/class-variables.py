# Class Variables are variables that are shared among all instances of a class

class Employee():

    num_of_emps = 0  # class variable to count the number of employees ie instances of the class
    raise_amount = 1.04 # this is a class variable

    def __init__(self, first, last, pay):
        #Attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        # Since the init method runs every time, we create a new employee, so we increment num_of_emps
        Employee.num_of_emps += 1 # we can use Employee instead self because in this case the num_of_emps don't change to each instance, it's the same value for all of them.

       
    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    def apply_raise(self): # using self instead the name of the class (Employee) allow us to overriden per instance if we needed
        self.pay = int(self.pay * self.raise_amount) # we need to either acess them through the class itself or a instance of the class (Employee/self)

emp_1 = Employee('Gabriele', 'Virgens', 5000) 
emp_2= Employee('Test', 'User', 6000)

# Shows the same values (the value of the class variable)
print(Employee.raise_amount) 
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print("\n")

# Print the instance attributes and your values
print(emp_1.__dict__)
print("\n")

# Print the attributes, variables, methods, ie all stuff of the class and your address memory
print(Employee.__dict__)
print("\n")

# We can acess and change the value of the class variables and it'll change the raise_amount fot he class and all of the instances
Employee.raise_amount =  1.05
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print("\n")

# We can also acess and change the value in a single instance
emp_1.raise_amount = 1.06 # when we did it we actually created the raise-amount attribute within emp_1
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print("\n")

# Checking the new attribute created through the dict with emp_1 namespaces 
print(emp_1.__dict__)
print("\n")

# Using the method apply_raise to raise the pay of the emp_1
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay) 
print("\n")

# Printing the number of employees
print(Employee.num_of_emps)