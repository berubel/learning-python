# Inheritance - Creating subclasses

'''Inheritance allows us to inherit attributes and methods from a parent class
and we can create sublcasses and get all the functionality of our parent class, 
the we can override or add completely new functionality without affecting the 
parent class in any way'''

# Classes are use case when we have differents groups with common characterists, such as employees with different roles
# We don't need to copy all common attributes and methods, just inherit it from the parent class to the subclass

'''Sometimes we want to initiate our subclasss with more information than our parent class can handle, so we can 
create a new init method for the subclass'''
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

class Developer(Employee): # Pass the parent class ie the class that we want to inherit as an argument to the subclass
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # We don't need to copy all of the init method and paste here. We want it to be as maintainable as possible
        # Just keep the init method of the parent class setting the common attributes, to do this, just call super()
        # and the init method. 
        super().__init__(first, last, pay,)
        # Another way to calling the parent is:
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # obs: we shouldn't to pass mutable data type like a list or dictionary as default argument
        if employees is None:
            self.employees = [] # equal to a empty list
        else:
            self.employees = employees  # equal to a employees list
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp)

# Creating instances of the subclasses that inherited your functionalitys from the Employee class
dev_1 = Developer('Gabriele', 'Virgens', 5000, 'Python') 
dev_2= Developer('Test', 'User', 6000, 'Java')

# The help function shows all kind of information about the Developer class 
# print(help(Developer))

print("\nDevelopers")
print("\n")
print(dev_1.email)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)

print("\n")
print(dev_2.email)
print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)
print(dev_2.prog_lang)

mgr_1 = Manager('Lisa', 'Smith', 9000, [dev_1]) # that manager supervise the dev_1 passed as an element of the list
mgr_1.add_emp([dev_2])
print("\nManagers\n")
print(mgr_1.fullname())
print(mgr_1.email)
mgr_1.print_emps() # print the employees that they currently supervise
print("\n")

# The function is instance will tell us if an object is an instance of a class
print(isinstance(mgr_1, Manager))
# The function is subclass will tell us if a class is a subclass of another
print(issubclass(Developer, Employee))