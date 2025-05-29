"""Accept name and age from the user. Check if the user is a 
 valid voter or not.
 Ex- “hello shery you are a valid voter”"""

name = input("please tell your name : - ")
age = int(input("Now, tell your age"))

if age >= 18 :
    print(f"hello {name} you are a valid voter")

else:
    print(f"hello {name} you are not a vaild voter")