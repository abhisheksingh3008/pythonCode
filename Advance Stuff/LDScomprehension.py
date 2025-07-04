# List, Dictionary and set comphrehension :----------------

"""
All of these Comprehensions are used to create List, Dictionary and set. But you do not 
have to use multiple lines of code for loops and If-Else statements........

"""
# Example of List comprehension :--------

l = [i for i in range(1,21) if i % 2==0]
print(l)

# Example of Dictionary comprehension :--------

l = {i : i**2 for i in range(1,11)}
print(l)

# Example of Set comprehension :--------

l = {i*i for i in range(10) if i % 2 == 0}
print(l)

