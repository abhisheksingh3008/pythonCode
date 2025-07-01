# Exception Handling 

"""
Error : 
       Errors occur due to mistakes in the code that prevent it from
       running. These can be syntax errors or logical errors.

Syntax Error :

print("Hello Abhishek"       # Missing closing parenthesis

Now this above code will give the error of syntax....

Indentation Errors :

def func():
print("Hello")                 # No indentation

There is one more tab error when you mix tabs and
spaces.

These errors cannot be handled. but what can be handled
are exceptions. 
                     
"""

"""
Exceptions :
            Exceptions are unexpected events or errors that occurs during the execution 
            of a program, which disrupts the normal flow of the program.....

            print("Start")    
            print("10/0")        # Raises zeroDivisionError
            print("End")         # This line will never run

            Now this is a ZeroDIvisionError and can be counted as Exception and because of this 
            exception the next line cannot be executed......

Exception Handling Keywords : 
                             try, except, else, finally, raise.......

            try : Wrap the block of code that might cause an exception

            except : Handle the exception if it occurs

            else : Run code only if no exception occurs

            finally : Run code no matter what, whether there is an exception or not

            raise : Manually throw an exception
"""

# Example....

a = int(input("tell your number :- "))

try:
    print(10/a)

except Exception as err:
    print(f"sorry there is an err as {err}")

print("ok I have done the division")

# or

a = int(input("tell your number :- "))

try:
    print(10/a)

except Exception as err:
    print(f"sorry there is an err as {err}")

else:
    print("Good there is no exception")

print("ok I have done the division")

# or 

a = int(input("tell your number :- "))

try:
    print(10/a)

except Exception as err:
    print(f"sorry there is an err as {err}")

finally:
    print("I will run no matter what?")

print("ok I have done the division")

# example of raise

age = int(input("tell your age :- "))

try:
    if age < 10 or age > 18:
       raise ValueError(" your age must be between 10 & 18")
    
    else:
       print(" Welcome to the club")

except Exception as err:
     print(f"An error occured as {err}")

print("The club will start soon")