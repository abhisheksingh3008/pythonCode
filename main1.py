print("Hii Abhishek")

"""variables"""

a = "Abhishek"       
age = 12                    # variables = a, age

"""NamingConvention"""

StudentName = "Abhishek"   # pascal case
studentName = "Abhishek"   # camel case
student_name = "Abhishek"  # snake case    

"""dataTypes"""
# Numbers
a = 12        
print(type(a))        # integer = 1,-1,0

b = 56.8
print(type(b))        # float = 1.1, p/q

c = 34j
print(type(c))         # complex

# Strings
st = '12345 abhsdicjvh !@#$% '     # use single('') or double ("") qutoes
print(type(st))

# Booleans
s = True
print(type(s))
t = False
print(type(t))

"""Strings"""
 # Unicode
l = "A"                
print(ord(l))

k = 65
print(chr(k))

# Indexing = always start from zero
name = "Abhishek Singh"     
print(name[1])
print(name[-3])             # Negative indexing start from -1

# String Slicing
name = "Abhishek Singh"
print(name[0:4:1])

""" TypeConversion """                 # two types = implicit / explicit
#explicit  = user use in build functions to convrts one data type to another
# int() / float() / str() / bool()
a = 12
a = str(a)
print(type(a))

# total falsy = 7 ( false, 0, 0.0, "", [], (), {} )

#implicit = python automatically converts one data type to another
a = 12

""" Output"""
name = "Abhishek"
age = 25
print(f"my name is {name} and my age is {age}")

"""Input"""
age = int (input("hello what is your age"))
print(age)

