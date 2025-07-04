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

"""
Class attribute : A normal variable created inside a class is a class attribute and thats it.....

Instance attribute : A attribute created using an instance like self.name, self.age etc. It is 
                     known as instance attribute.....

"""
# Example......

class Car:
    wheels = 4         # Class Attribute

    def __init__(self, color):
        self.color = color        # Instance Attribute


# Types of Methods.....

"""
Instance Method : An instance method Works with instance (object) of the class. 
                  This method can access and modify instance attributes.......

"""

# Example.....

class MyClass:
    def instance_method(self):
        print("This is an instance method")

"""
Class Method : This method works with the class itself it will not target the 
               instance (object). we have to use @classmethod decorator for 
               creating the class method and it takes cls as their first parameter.....

Static Method : This method does not access class or instance directly it 
                also uses a decorator @staticmethod it just acts like a 
                regular function placed inside a class..... 
"""
    
# Example of class Method    

class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method")

# Example of Static Method  

class MyClass:
    @staticmethod
    def static_method():
          print("This is a static method")


" 4 pillers of OOps "

# Inheritance...... 

"""
In general terms Inheritance means property or any possession that comes to an heir...

It works between classes. Inheritance allows a class (child class) to inherit properties and
behaviors (attributes and methods) from another class (parent class).....

Benefits of using inheritance is :
                                  Code reusability
                                  Organized structure
                                  Easy to maintain and extend

"""

# Syntax of Inheritance :

"""
Syntax is very simple just like you take parameters in functions here 
you will take parameters but those parameters will be classes......

"""

# Example.....

class FactoryMumbai:   # Parent class / super class
    a = "I am an attribute mentioned inside FactoryMumbai "
    def hello(self):
        print("hello I am a method mentioned inside FactoryMumbai ")

class FactoryPune(FactoryMumbai):        # Child class / sub class
    pass

obj = FactoryMumbai()
obj2 = FactoryPune()

obj2.hello()
print(obj.a)


# Constructor in Inheritance

"""
Lets say you have created a parent class with a constructor function inside it and
then this class is inherited by another class then the constructor function of
parent class will work for the child class as well....

"""

# Example.....

class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")

class Human(Animal):
    pass

animal1 = Animal("lion")
person1 = Human("Abhi")

person1.show()

"""
Now lets say you need a new parameter in your child class you have to create a 
constructor function for your child class but the parameters that can be 
initialized in the parent class will be initialized using the super() function. 
Super function will target the parent class....

"""
# Example.....

class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")

class Human(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"hello your name is {self.name},{self.age}")
        
animal1 = Animal("lion")
person1 = Human("Abhi", 25)

person1.show()

# Types of Inheritance 

"""
Single Inheritance :
                    All the inheritance we saw above was single level....

Multiple Inheritance : 
                      Multiple Inheritance means there will be 2 parent classes and only 1 
                      child class and the child class will inherit all the attributes and 
                      methods of both parents....

Multilevel Inheritance : 
                        This is a basic case where we will have....
                            * grandparent class → parent class → child class
                            * The attributes and methods are passed on through all the classes

"""

# Example of Multiple Inheritance....

class Animal:
    name1 = "lion"

class Human:
    name2 = "Abhi"

class Robots(Animal,Human):
    name3 ="charli123"

obj = Robots()

print(obj.name1)
print(obj.name2)
print(obj.name3)

# Example of Multilevel Inheritance....

class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

obj = PuneFactory("nylon",20,"Red",30)

print(obj.material)

# Polymorphism......

"""
Polymorphism is a core concept in (OOP). The word means "many forms" — and in programming, 
it allows the same interface or method name to behave differently depending on the 
object or context.....

"""

# Types of Polymorphism......

"""
Polymorphism can be achieved in python in two ways well if we talk about compile time 
languages there are 3 ways but python does not support Method overloading......

Method overloading means having same name methods inside a class but parameters will 
be different but in python the latest definition will overwrite the previous one....

Method Overriding :
                   This is where a child class overrides a method of the parent class, and Python 
                   decides at runtime which method to call, based on the object type......

Duck Typing : 
             Python follows the philosophy:
            “If it walks like a duck and quacks like a duck, it must be a duck."

"""
# Example of Overriding......

class Animal:
    def show(self):
        print("Helo I am abhi")

class Human(Animal):
    def show(self):
        print("how are you")

obj = Human()
obj.show()

# Note : Method Overloading......(Python not supported)

# Example of Duck typing......

class Animal:
    def show(self):
        print("I am showing")

class Human:
    def show(self):
        print("I am also showing")

obj = Animal()
obj1 = Human()

obj.show()
obj1.show()

# Encapsulation.........

"""
Encapsulation means putting data (variables) and code (functions) together 
in one place — inside a class.....

It also means hiding the internal details of how things work, and
only showing what is needed.......

It keeps data safe from being changed by mistake....
It makes your code clean and easy to use....
It gives control over what others can access or change...

"""

# Access modifiers in python.......

"""
Access modifiers means how we give access of our attributes and methods to the 
object or inherited classes. There are 3 types lets see them one by one......

Public Attributes and Methods :-----------

Till now every attribute and methods we have created are public means the 
inherited classes and objects can access them no matter what....

Protected Attributes and Methods :-------------

python protected members are created using a single underscore but it still can be accessed 
from outside the class so you might wonder whats the point of using them....

Python does not enforce protected access like other languages (e.g., Java or C++). 
But it uses a naming convention to tell developers....

Private Attributes and Method :------------

A private variable or method means : 

It cannot be accessed from outside the class — only from inside 
the class where it is defined....

In Python, we use two underscores (__) before the name to
make it private.....

"""
# Example of Public Attributes & Method.....

class Factory:
    a = "Pune"

    def show(self):
        print("Hello i am a pune factory")

class Bhopal(Factory):
    def show2(self):
        print("super().a")

obj = Bhopal()
obj.show2

# Example of Protected Attributes & Method.....

class Factory:
    _a = "Pune"

    def show(self):
        print("Hello i am a pune factory")

class Bhopal(Factory):
    def show2(self):
        print("super()._a")

obj = Bhopal()
obj.show2

# Example of Private Attributes & Method.....

class Factory:
    __a = "Pune"

    def show(self):
        print("Hello i am a pune factory")

class Bhopal(Factory):
    def show2(self):
        print("super().__a")

obj = Bhopal()
obj.show2

# Abstraction.........

"""
Abstraction does not exist in python but we can achieve it using a
library we will see what is a library later......

Abstraction is used to simplifying complex systems by focusing
on essential features and hiding unnecessary details.....

It is used to define a common interface for different subclasses....

Abstract classes and methods :-----------

Abstract classes are classes that contains one or more abstract methods......

A method that is defined but not implemented in the abstract class. 
subclasses must provide the implementation......

"""

# Example of Abstract.......

from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(abstract):
    def __init__(self,side):
        self.side = side

    def perimeter(self):
        print("I have created")

    def area(self):
        print("I have created this")

class Circle(abstract):
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        print("I have created")

    def area(self):
        print("I have created this")

obj = Circle(7)
obj2 = Square(12)

# Dunder methods.........

"""
Dunder methods are special methods in Python that start and end with double 
underscores, like __init__, __str__, __add__, etc.......

They automatically get called when you perform certain actions
on an object.....

They help you:
              Customize behavior of your class....
              Make your class objects behave like built-in data types (like strings, lists, etc.)..
              
"""

# Example of Dunder Method........

class Animal:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Hello how are you and your name is {self.name}"
    
obj = Animal("lion")

print(obj)
       

