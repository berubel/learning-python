#PYTHON BASICS

#Variables
age=20
price = 19.95
first_name = 'Mosh'
is_online = True #case sensitive, letra maiuscula é necessário
state = 'new pacient'

print("Hello World") #posso usar tanto uma '' quanto ""
print("\n")
print(age)
print(price)
print(first_name)

if is_online == True:
    print(state)

#Input - Get the value input on the terminal and save it

name = input("\nWhat is your name? ")
print("Hello " + name) #concatenation

#Type conversion

birth_year = input("\n\nEnter your birth year: ")
age = 2022 - int(birth_year) #conversion is necessary, cuz the function returns a string value
print(age)

first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("Sum: "+ str(sum)) #converte de float para str para ser possível concateanr

#String

course = 'Python for Beginners' #a object
print(course.upper()) #a method for let the string in upper case
print(course)
print(course.find('y')) #busca um dado na string e retorna o indice de onde se encontra (no caso 1)
print(course.replace('for', '4')) #substitui uma sentença por outra
print('Python' in course) #print if the sentence was found in the object str

#Arithmetic Operators

print(10+3) #addition
print(10-3) #subtraction
print(10*3) #multiplication
print(10/3) #division with many numbers after the dot
print(10//3) #division without numbers after the dot (return a integer)
print(10 % 3) #returns the remaint of the division
print(10 ** 3) #returns the result of the power
x=10
x += 3 # value x +3, or another operators
print(x)

#Operator Precedence

x = 10 + 3 * 2
print(x) # 16
x = (10 + 3) * 2
print(x) # 26

# Comparison Operators

x = 3>2 #boolean expression, returns a boolean value
print(x)
x = 3==2
print(x)
x = 3!=2
print(x)

#Logical Operators
price = 25
print(price > 10 and price < 30) #and == && operator
print(price > 10 or price < 30) #or == || operator
print(not price < 30) #not == !! operator inversus of any value that u have given

#if statements

temperature = 25

if temperature > 30: #indented represents the lines is in the block of code
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("\nDone")

#While loops

i = 1
while i <= 5:
    print(i * '*') #multiplica a quantidade de asteriscos por i a cada iteration
    i += 1

#Lists

names = ["John", "Bob", "Mosh", "Sam", "Mary"] #similiar a vetores
print(names)
print(names[0]) #to gete a especific name insert the index of the element
print(names[-1]) # print the last element of the list
print(names[-2]) # second element of the end of the list
names[0] = "Jon"
print(names)
print(names[0:3]) #print the start index to the end index, the elements in a range

#List Methods

numbers = [1,2,3,4,5]
numbers.append(6) #add in the final
numbers.insert(0,-1) #insert in the init
numbers.remove(3) #remove a element
numbers.clear()  #clear the list
print(numbers)
print(1 in numbers)
print(10 in numbers)
print(len(numbers)) #show the lenght of the list

# For loops

numbers = [1,2,3,4,5]
for item in numbers: #printa os itens presentes na lista até o ultimo item
    print(item)

#The range function

numbers = range(5) # a sequence of numbers
numbers = range(5,10) # a sequence of numbers that start at five and end at 10
numbers = range(5,10, 2) # a sequence of numbers that start at five and end at 10, but stops at the index two
print (numbers)

for number in numbers:
    print(number)

#Tuples

numbers = (1,2,3,3) #parenteses is a tuple
 #uples are unchangeble, imutable
numbers.count(3) #returns the quantity of elements 3 exists in the tuple
numbers.index(2) #returns the index of a first occurrence of a element

#Functions

def hello_func(greeting, name='You'):
   # print("Hello")
   return '{}, {}.'.format(greeting, name) #adiciona o elemento presente no argumento a frase

#hello_func()
#print(hello_func().upper())
print(hello_func('Hi'))
print(hello_func('Hi', name = 'Corey'))

def student_info(*args, **kwargs): #args representa um conjunto de argumentos e kwargs outro conjunto
   print(args)
   print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(*courses, **info)