# Args and Kwargs :------------ 

"""
They are special keywords in Python used in function definitions to
accept a flexible number of arguments......

Now you always do not have to use Args and Kwargs the main thing is * , ** 
you can use any names in front of them.......

so *args are used for multiple positional arguments, and **kwargs are 
used for multiple key word arguments......

And the *args becomes a tuple and **kwargs becomes a dictionary.......

"""
# The use case is great :--------

"""
You do not need to know how many inputs you'll get.....

Helps in building flexible functions, decorators, APIs, and more...

"""

# Example of args :---------

def addition(*args):
    sum = 0
    for i in args:
        sum = sum + i

    print(sum)

addition(12,13,14,15)

# Example of kwargs :---------

def information(**kwargs):
    print("your information is\n\n")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

information(name = "Abhishek Singh", age = 25, designation = "Data Analyst")