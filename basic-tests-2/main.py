#Ternary if statements
number = 10
message = "positive" if number > 0 else "0 or negative"
print (message)

#That's equals to (only if u have one if and an else)
if number > 0:
    print("positive")
else:
    print("0 or negative")

#Lists

# It's possible to have an list inside another list
numbers = [1, 2, 3, 4, -1, -20, ["A", "B"]]
#To acess the internal list, just indicate the index where it starts
print(numbers[6])
#Acess a specific element of the internal list by the index
print(numbers[6][0])

#List Methods

#Remove an element
numbers.remove(["A", "B"])
print(numbers)
#Sort the elements of the list
numbers.sort()
print(numbers)
#Reverse the list
numbers.reverse()
print(numbers)
#Add an element to the end of the list
numbers.append(1000)
print(numbers)
#Show the lenght of the list (size)
print(len(numbers))
#If an element is in the list (returns a boolean value)
print(5 in numbers)
#If an element is not in the list (returns a boolean value)
print(5 not in numbers)
#Removes the last element
numbers.pop()
print(numbers)
#Removes by the index
del numbers[0]
print(numbers)
#Removes a range (it's not index based) by the index
del numbers[0:2]
print(numbers)

numbers.append(50)
numbers.append(70)
numbers.append(-5)
print(numbers)

#Sets

# In Sets duplicates are not allowed
numbersList = [1,1]
numbersSet = {1,1}
lettersSet = {"A", "A", "B", "C"}
#The difference between set and list, is the order is the not garantee
print(numbersList)
print(numbersSet)
print(lettersSet)

#Set union, intersection and difference

lettersA = {"A", "B", "C", "D"}
lettersB = {"A", "E", "F"}
#Union (merge the sets)
union = lettersA | lettersB
print(f"Union = {union}")
#Intersection (returns the occurrences in both sets)
intersection = lettersA & lettersB
print(f"Intersection = {intersection}")
#Difference (returns what is just on the right set)
difference = lettersA - lettersB
print(f"Difference = {difference}")

#Dictionaries

#It's a key:value pair data structure (the keys must be unique)
person = {
    #key   :  value
    "name": "Jamal",
    "age": 20,
    "address": "USA"
}
#print the value by the key
print(person["name"])
print(person["age"])
print(person["address"])
#show the keys of the dictionary
print(person.keys())
#show the values of the dictionary
print(person.values())
# Another way of getting
print(person.get("age"))
# Update data
person["age"] = 100
print(person.get("age"))
#clear the dictionary
#person.clear()
print(person)

#For loop

names = ["Ahamed", "Annah",
         "James", "Jamila"]

#Loop through dictionaries

# Print the keys of the dictionary
print("\nPrint keys")
for key in person:
    print(key)

#Print the keys and values
print("\n\nPrint keys and values")
for key in person:
    print(f"key: {key} value: {person[key]}")

#Better way to print the keys and your values
print("\n\nAnother way to print keys and values")
for key, value in person.items():
    print(f"key: {key} value: {value}")

#Items returns the key and value combinated
print("\n{}\n".format(person.items()))

#Exercise
result = 0
numbers = [1, 3, 5, 6, 7, 9]
print("{}\n".format(numbers))
for number in numbers:
    result += number
    print(number)
print(f"\nResult = {result}\n")

#While loop

i = 0

while i < 10:
    print(i)
    i += 1
else: #If the condition is not true anymore
    print("while loop ended")

#Break and continue

number = 0
#Print while number is different of 5, if is equals to 5 then break the loop
print("\nBreak")
while number < 10:
   if number == 5:
       break
   number += 1
   print(number)
print("\nContinue")
#Continue the iteration if the condition is true
number = 0
while number < 10:
   number += 1
   if number < 5: #Restart the loop to the beggining
       continue
   print(number)

#For loop with continue
print("\n")
for n in [1, 2, 3, 4, 5, 6, 7,]:
    if n < 5:
        continue
    print(n)

#For loop with break
print("\n")
for n in [1, 2, 3, 4, 5, 6, 7,]:
    if n == 5:
        break
    print(n)

#Functions

def greet():
    print("\nHello how are you?\n")

greet()

#Parameters and arguments

def hi(name, age):
    print("Hello {} how are you?".format(name))
    if age >= 0:
        print("I know your age is {}".format(age))

hi("Sakura",5)
hi("Alfredo", 2)

#Return values from functions
print("\n")
def is_adult(age):
    if age >= 16:
        print("adult: age is {}".format(age))
        return True
    else:
        print("not yet an adult: age is {}".format(age))
        return False
is_adult(45)
result = is_adult(10)
print(result)
print("\n")

def convertGender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return "Gender {} is a unknown.".format(gender)

print(convertGender("F"))
print(convertGender("f"))
print(convertGender("M"))
print(convertGender("s"))

#Built in functions and import statement
print("\n")
#import modules
import math
#import a function of a module, and not bring the entire module
from math import isqrt
#Using methods of math function
print(math.pi) #returns pi number
print(math.isqrt(16)) #returns the square root

#Creating modules
print("\n")
#importing your own code created in the new file
import calculator
#if u only need a unique method, import the only one
from calculator import divide

print(calculator.add(2,2))
print(calculator.subtract(2,2))
print(calculator.divide(2,2))
print(calculator.multiply(2,2))

#Classes and Objects

class Phone:
    #constructor
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    #behavior
    def call(self, phone_number):
        print("{} is calling {}".format(self.brand, phone_number))
    #To string method
    def __str__(self) -> str: #this arrow "->" means the method returns a str data type
        return "Brand {} \nPrice = {}".format(self.brand, self.price)


#Instances
iphone = Phone("Iphone 13", 2500)
samsung = Phone("Samsung S20", 2000)
print("\n")
#Properties
print(iphone.brand, iphone.price)
print(samsung.brand, samsung.price)
#Behaviour
iphone.call("999")
samsung.call("55555")

#Printing Objects
print("\n")
#This way of printing just shows the memory address where the object is. It's necessary to hava a "To string" method
#to show the correct values of the objects
print(iphone)
print(samsung)
print("\n")

#Working with dates
print("\n")

from datetime import datetime
from datetime import date

#Without import the specific function
#print(datetime.datetime.now())
#print(datetime.date.today())
#print(datetime.datetime.now().time())

#With import the specific function
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(date.today())
print(datetime.now().time())

#Formating dates

now = datetime.now()
print(now)
#Returns the format date
print("\nFormated date")
print(now.strftime("%d/%m/%Y %H:%M:%S"))
#Returns the format date with the name of the month
print(now.strftime("%d/%B/%Y %H:%M:%S"))
#Returns the format date with the abreviation of the month
print(now.strftime("%d/%b/%Y %H:%M:%S"))
#Print and format the date
print(date.today().strftime("%d/%m/%Y"))
#Print and format the hour
print(datetime.now().time().strftime("%H:%M:%S"))

#Creating Files

# w = writing
# a = appending
# r = reading
# r+ = reading/writing

#creates a file that dooesn't exist
f = open("./data.csv", "w")

#open the file to reading and writing
#f = open("./data.csv", "r+")
#f.write("id, name, email\n")
#f.write("1, Bel, berubel@gmail.com\n")
#f.write("2, Sakura, sakurin@gmail.com\n")

#Always you work with files is necessary close them
#f.close()

#open the file to reading
#f = open("./data.csv", "r")

#Open the file and update (appended/add) the data
#f = open("./data.csv", "a")
#f.write("3, Alfredo, lilou@gmail.com\n")
#f.close()

#open the file to reading and writing (override)
f = open("./data.csv", "r+")
f.write("id, name, email\n")
f.write("1, Bel, berubel@gmail.com\n")
f.write("2, Sakura, sakurin@gmail.com\n")
f.write("3, Alfredo, lilou@gmail.com\n")
f.write("4, Eloise, elo@gmail.com\n")
f.close()

#Reading from files
#print("\n")
#f = open("./data.csv", "r")

#Read the entire file
#print(f.read())

#Read the first line of the file
#print(f.readline())
#f.close()

#Line in file loop
#for line in f:
#    print(line)
#f.close()

#Returns a list with each line
#print(f.readlines())
#f.close

#A better way to work with files

#with sintax remove the need to use "close file", cuz it's automatically done

import os.path
print("\n")
filename = "./data.csv"
#check if the file exists or not, both objects have same name(value), prevents error
if os.path.isfile(filename):
    with open("./data.csv", "r") as file:
        print(file.read())
else:
    print("File {} does not exist".format(filename))

#Fetching data from internet

from urllib import request
import json
import requests
import pyttsx3

#r = request.urlopen("https://www.google.com")
#Make a request and gets a http response by the client
#print(r)
#Returns a number if the request was find so u can read the data
#print(r.getcode())
#Shows a string with the code of the web page
#print(r.read())

#Fetching Jokes from internet

# Using urllib

#url = "http://api.icndb.com/jokes/random/3"
#r = request.urlopen(url)
#print(r.getcode())
#data = r.read()
#json_data = json.loads(data)
#print(json_data)

# Using requests from pip
url = "http://api.icndb.com/jokes/random/3"
response = requests.get(url)
print(response.status_code)
#data = response.text
json_data = json.loads(response.text)
print(json_data)

class Joke:

    def __init__(self,  joke):
        self.joke = joke


    def __str__(self) -> str:
        return "joke {} ".format( self.joke)


jokes = []

for j in json_data:
    joke = json_data["value"]
    joke = Joke(joke)
    jokes.append(joke)

print(len(jokes))

for joke in jokes:
    print(joke)
    print("\n")

#Text to speech
#pyttsx3.speak(json_data)

