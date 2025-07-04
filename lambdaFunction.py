# Lambda Function :----------------

"""
A lambda function is an anonymous, inline function defined using the lambda keyword.......

It's often used for short, simple functions that are used only once or temporarily.......

You can have multiple arguments but there will be only one expression..........

"""

# Example ofLambda Function :-------

addition = lambda a,b : a+b
print(addition(12,13))

# Example using if else in lambda function :----------

addition = lambda a : "even" if a % 2 == 0 else "odd"
print(addition(12))