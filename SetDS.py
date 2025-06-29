" Set DS Basics "

# Tuple have the 4 features are Mutable, Duplicates, Unordered, Heterogenous

"""  
Mutable : Sets are mutable you can change the values of
set.

Duplicates : You cannot have any duplicate values in set
that means every element will be unique.

Unordered : Sets are unordered and you cannot access
them through index values.

Heterogenous : Set is semi-heterogenous it can store
some data types like string, numbers, tuples but not
everything.

"""
# create a Set we have to use square brackets ({}).

s = {1,2,3,4,5,6,7,8,9}
print(type(s))  # output : set

"""
 How Set stores value in python :-

Each value in a set is hashed using a hash function (hash() in
Python).
The hash is used as an index to store the element in memory.

"""

b = hash("hello")
print(b)

c = hash((1,2,30))
print(c)

# Set methods :-

# add() : adds an element to the set
# remove() : removes element  { raises an error if not found element}
# discard() : removes element  { No error if not found element}
# pop() : remove a random element
# clear() : remove all elements

""" Sets also have some special methods for performing some special operations between 2 sets. """

a = {1,2,3,4,5}
b = {4,5,6,7,8}

union_set = a.union(b)
print(union_set)             # print(a|b) union

intersection_set = a.intersection(b)
print(intersection_set)                 # print(a & b) intersection

difference_set = a.difference(b)
print(difference_set)                    # print(a - b) difference

symmetric_diff = a.symmetric_difference(b)
print(symmetric_diff)                        # print(a^b) symmetric diff