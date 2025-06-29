""" Data Structures """

""" Data structures are used to store, organize, and manipulate
    data efficiently. Python provides several built-in data
    structures """

""" Now in python we have 4 types of in-build data structure
    List, Tuple, Dictionary, Set """

" List DS Basics "

# List have the 4 features are Mutable, Duplicates, Ordered, Heterogenous

# create a list we have to use square brackets ([]).

"""
Mutable - Mutability refers to whether an object's value
can be changed after creation. And List allows this.

Duplicates - we know data structures are used to store
multiple values so duplicates means same value occuring
multiple time. List allows this.

Ordered - List maintains ordered data structure maintains
the sequence of elements as they were inserted. This
means you can access elements using their position
(index).

Heterogenous - List have heterogenous nature that means
we can have multiple data types inside the list.

"""

# Ex:  fruits = ["apple", "banana", "orange"]
#      numbers = [10, 20, 2, 40]

numbers = [20, 10, 30, 66, 40]
numbers[3] = 70
print(numbers)

# List Traversing and methods 

a = [20, 10, 30, 66, 40, 30.5]
# 1st way using index

for i in range(len(a)):
    print(i)
    print(a[i])

# 2nd way directly on value

for i in a:
    print(i)

""" Method = kind of function """

print(dir(list))  #  all of the method and function of the list

l = [1,2,3,4,5,6,7]

# The append() method in Python is a built-in function used to add a single element to the end of an existing list.

l.append(10)
print(l)

# the insert() method is a built-in list method used to add an element at a specific position (index) within a list.

l.insert(1,44)
print(l)

# the extend() method is a built-in list method used to add all elements from an iterable (such as another list, tuple, or string) to the end of the current list.
p = [22,33,44]
l.extend(p)
print(l)

# the remove() method is used to remove a specific element from a list or a set.

my_list = ["apple", "banana", "cherry", "banana"]
my_list.remove("banana")
print(my_list)

# The pop() method in Python is used to remove an item from a collection and return the removed item.


my_list = [10, 20, 30, 40]
removed_item = my_list.pop(1) # Removes element at index 1 (20)
print(my_list) # Output: [10, 30, 40]
print(removed_item) # Output: 20

last_item = my_list.pop() # Removes the last element (40)
print(my_list) # Output: [10, 30]
print(last_item) # Output: 40

# index() function is a useful tool for finding the index of a specific element in a sequence.

# The count() function in Python is a built-in method used to determine the number of occurrences of a specific element within a sequence.

my_list = [1, 2, 3, 1, 2, 1, 4]    
count_1 = my_list.count(1)
print(count_1)

# Sorts the list in ascending order

my_list = [5, 2, 8, 1, 9]
my_list.sort()  # Sorts in ascending order
print(my_list)  # Output: [1, 2, 5, 8, 9]

my_list.sort(reverse=True) # Sorts in descending order
print(my_list) # Output: [9, 8, 5, 2, 1]

words = ["apple", "banana", "kiwi", "grape"]
words.sort(key=len) # Sorts by string length
print(words) # Output: ['kiwi', 'grape', 'apple', 'banana']

# reverse the list order

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]

# copy : creat the copy of the list

original_list = [1, 2, [3, 4]]
copied_list = original_list.copy()
print(f"Original: {original_list}")
print(f"Copied: {copied_list}")

copied_list.append(5)
copied_list[2].append(99) # Modifies the nested list in both
print(f"Original after modification: {original_list}")
print(f"Copied after modification: {copied_list}")

# clear : remove all element from the list 

list = [1, 2, 3, 4, 5]
list.clear()
print(list) # Output: []