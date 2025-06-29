" Tuple DS Basics "

# Tuple have the 4 features are Immutable, Duplicates, Ordered, Heterogenous

"""  
Immutable : Tuple are immutable you can not change the values of
tuple.

Duplicates : You can have duplicate values in tuple there
are no restriction.

Ordered : Tuple are ordered and you can access them
through index values.

Heterogenous : Tuple also have heterogenous nature and
can have different types of data structure in tuple.

"""

# create a Tuple we have to use square brackets (()).

tup = (2,3,4,5,6)
print(type(tup))

#  Methods of tuple are : index() & count() [tuple have only two methods]

# index() : find the index

t = (1,3,2,3,4,5,6,7,8,9)
index = t.index(3)
print(index)

# count() : count the occurances

t = (1,3,2,3,4,5,6,7,8,9,9,9,8)
count = t.count(9)
print(count)

# tuple unpacking

t,a,s,d = (1,2,3,4)
print(t)
print(a)
print(s)
print(d)

a = (1)
print(type(a))   # output = int

a = (1,)
print(type(a))   # output = tuple