"""Accept the gender from the user as char and print the respective greeting message
 Ex - Good Morning Sir (on the basis of gender)"""

gen = input("please tell your gender as character (M or F):-")

if gen == 'M' or gen == 'm':
    print("Good morning Sir")
elif gen == 'F' or gen == 'f':
    print("Good morning Maam")    

else:
    print("Unidentified gender")