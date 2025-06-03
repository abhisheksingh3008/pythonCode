""" Count all letters, digits, and special symbols from a given
string
 Given: str1 = "P@#yn26at^&i5ve"
 Expected Outcome:
 Total counts of chars, digits, and symbols
 Chars = 8
 Digits = 3
 Symbol = 4"""

a = "gr9yt755749rh!@#$%6"

char = 0
dig = 0
spchr = 0

for i in a:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        spchr += 1

print(f" Your digits are {dig} \n Your alphabates are {char}\n Your ecial characters are {spchr}")


