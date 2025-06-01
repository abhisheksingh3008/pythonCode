# For Loop

"""Syntax of range function is simple range(start, stop, steps)
you have 3 points from where you want to start, till where
you want to stop and how many steps you want#
If you don’t mention start point the default value will be 0 .
if you don’t mention the steps the default steps will be 1.
you have to mention the stop point otherwise the range 
function will not work."""

a = range(1,21,1)

for i in a:
    print(i)

# 2nd Method to write for loop

for i in range(1,21,1):
    print(i)

# Start default value 0, Step default value 1

for i in range(21):
    print(i)

# Counting number in back side

for i in range(16,0,-1):
    print(i)

for i in range(-5,-16,-1):
    print(i)

# lets print a table of 5

for i in range(5,51,5):
    print(i)

# take input

n = int(input(" which table you want? "))

for i in range(n, (n*10)+1, n):
    print(i)

"""Loop for string"""

a = "Abhishek"

for i in range(0,8,1):
    print(a[i])

# Given Any Sentences

a = "Abhishek is a good boy"
print(len(a))

for i in range(len(a)):
    print(a[i])

a = "Abhishek"

for i in a:
    print(i)

""" Break / Continuous / Else  in Loop"""

# Continue 

for i in range(1,21):
    if i == 15:
        continue
    print(i)

# Break

for i in range(1,21):
    if i == 15:
        break
    print(i)

# Else

for i in range(1,21):
    if i == 15:
        print("break statement is executed")
        break
    print(i)

else:
    print("break statement is not executed")

########

for i in range(1,21):
    if i == 56:
        print("break statement is executed")
        break
    print(i)

else:
    print("break statement is not executed")
    
        