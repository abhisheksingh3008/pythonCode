" Decorator "

"""
A decorator is just a function that modifies another function without changing its actual code....

"""
# Example of Decorator......

def decorate(func):
    def wrapper(a,b):
        print("the addition to your numbaers are")
        func(a,b)
        print("thankyou I hope you liked it")
    return wrapper

@decorate
def addition(a,b):
    print(f"your total is {a + b}")

addition(12,88)
