"""Check string is Pallindrome or not """

a = input("Give a string : ")

b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]

if a == b:
    print("Your string is pallindrome")

else:
    print("its not a pallindrome")