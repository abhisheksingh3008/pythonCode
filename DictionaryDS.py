""" Dictionary DS Basics """

# Dictionary have the 4 features are Mutable, Duplicates, Ordere, Heterogenous

"""
Mutable : Dictionaries are mutable, meaning you can change, add, or 
          remove key-value pairs after creation.

Duplicates : Keys must be unique, but you can have
             duplicates in values.

Order : Dictionary follows insertion order.

Heterogenous : A dictionary can store different types of keys and values, like integers, 
               strings, lists, or even another dictionary.
 
"""
# Important :  This DS called hash map in other language but in python call Dictionary......

" Dictionary syntax and working "

# Now we know we have to use key and value pairs to store values in dictionary.
# The keys in dictionary acts like index values that we use in List.

" Example "

admin = {"name" : "Abhishek", "age" : 25}
print(admin["age"])      # output : 25
print(admin["name"])      # output : Abhishek

d = {10:100,20:200,30:300,40:400}
print(d[10])
print(d[40])

d[10] = 1000   # Update
print(d)
d[50] = 500    # Create
print(d)

d.update({50:500})
print(d)

del d[30]   # Delete
print(d)

""" Again telling we can perform CRUD(create, read, update, delete) operations on 
    values but not all on keys cause the keys cannot be changed after creation...
"""

" Dictionary traversing "

""" We can traverse both keys and values in dictionary, but default loop is set on keys and you can
    access the valuesbecause of keys.
    So technically you can traverse on both keys and values at the same time......
 """

" Example "

num = {1:10, 2:20, 3:30, 4:40}

for i in num:
    print(i, ":", num[i])

# help(dict) use for show all dictionary method in your terminal
