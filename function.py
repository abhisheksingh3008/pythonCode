"""Function"""

""" Functions in Python group reusable code into a block that
    can be executed by calling the function name. This helps
    avoid repetition and makes programs modular and readable. """

# Parameters :- Parameters are variables listed inside the function definition. 
# Arguments :- Arguments are the Values passed to a function when it is called.

def greet(name):        # name = Parameter
    print(f"Hello {name}! how are you")

greet("Abhishek")         # Abhishek = Argument

"""-----------------------------------------------------------"""

# Types of Arguments

# 1. Positional Arguments

def hello(name, age):
    print(f"your name is {name} and your age is {age}")

hello(age = 25,name = "ABhi")

"""------------------------------------------------------------"""

def pallindrome(str):
    rev = ""
    for i in range(len(str)-1,-1,-1):
        rev = rev + str[i]

    if rev == str:
        print(f"{str} is a pallindrome")
    else:
        print(f"{str} is not a pallindrome")

pallindrome("NAMAN")
pallindrome("Abhshek")

"""-----------------------------------------------------------"""

# Return function

def hello():
    return "Hello how are you?"

print(hello())