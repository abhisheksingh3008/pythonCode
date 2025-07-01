""" OOPs in Python """

"""
oops :- OOPS (Object-Oriented Programming System) is a programming paradigm based on the concept 
        of "objects", which can contain data (attributes) and code (methods)..

"""

# Example.......

class Addition:
    def __init__(self, a, b):
        print(a + b)

obj = Addition(12, 12)

""" Classes in OOPs """

"""
Class :- A class is like a blueprint or template for creating objects...
         
         Think of a class like the blueprint of a house. It defines what the house should have 
         (rooms, windows, etc.) but does not tbuild the house. An object is the actual house 
         built using that blueprint.....
"""

# Syntax of class

"""
A class is also created with a basic keyword class and a name in front of it.....

class Car:
    brand = "Toyota"

Creating a class is super simple now lets see what is inside class...... 
There are 2 types of things inside class Attributes and Methods.........

Attributes - Variables defined inside the class are Attribute.....

Methods - Functions defined inside a class are Methods.....
    
"""

# Example......

class Animal:
    species = "Dog"      # Attribute

    def make_sound(self):    # Method
        print("Bark!")

print(Animal().species)

Animal().make_sound()


""" Objects in OOPS """

"""
Object syntax :
               It is very easy to create an object you just have to call the class inside a 
               variable and that variable becomes an object....

               The object has all the powers of a class therefore a class object can access 
               attributes and methods of a class.....
          
"""

# Example......

class Fruit:
    name = "Apple"

# creating an object
f = Fruit()

# Accessing the attribute

print(f.name)

""" Constructor """

"""
A constructor is a method that runs automatically when we call a class and this 
constructor function will target the objects location.......

To target the objects location we use self keyword......

"""

# Example......

class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"your object details are {self.material}, {self.zips}, {self.pockets} ")

reebok = Factory("leather",3,2)

campus = Factory("nylin",3,3)

print(campus.pockets)

reebok.show()

""" Attributes and Methods """

# Types of Attribute.....

