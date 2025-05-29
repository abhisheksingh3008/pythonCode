"""Accept a year and check if it a leap year or not (google to 
 find out what is a leap year)"""

year = int(input("tell your year :- "))

if year % 100 == 0 and year % 400 == 0 :
    print("Its a leap year")

elif year % 100 != 0 and year % 4 == 0:
    print("Its a leap year")

else:
    print("Its a normal year")