# File Handling 

"""
File Handling :-
                File handling means Creating, Reading, Updating, Deleting(CRUD) operations 
                that we can perform in files....

                We have to use open() function to open a file in python.

"""
# Example.....

p = open('exceptionHandling.py')
print(p.read())                     # read entire file

"  Now there are multiple modes to open the file....."

#     Mode      Description
"     'r'   :   Read(default) - file must exist..."
"     'w'   :   Write - creates file or overwrites..."
"     'a'   :   Append - adds to end of file..."
"     'x'   :   Create - creates a new file, fails if it exists..."

# Example.....

r = open("superman.txt",'w')

r.write("Hello this side abhishek and i am writing inside thhis file..")

r.close()

# ............................................................

r = open("superman.txt",'a')

r.write("and now i am appending some content inside the file...")

r.close()


