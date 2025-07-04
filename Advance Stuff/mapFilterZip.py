# Map Filter Zip :---------------

"""
Map is used for applying a function to multiple items......

Takes a list (or any sequence).....

Applies the same function to every item in that list.......

Gives you back a new list (in Python 3, it gives a map object
which you can convert to a list)......

"""
# Example of map() function :---------

a = [1,2,3,4,5]

result = map(lambda x : x*2, a)
print(list(result))

# Filter :-----------

"""
Filter as the name suggest is used to filter out the stuff.........

Takes a list (or other sequence).........

Checks each item using a function (a test)......

Keeps only the items that pass the test (i.e., return True)......

"""
# Example of filter() function :---------

def even(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
a = [1,2,3,4,5,6,7,8,9]

result = filter(even, a)
print(list(result))

# or :--------------

a = [1,2,3,4,5,6,7,8,9]

result = filter(lambda x : True if x % 2 ==0 else False, a)
print(list(result))