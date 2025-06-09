""" Separate each digit of a number and print it on the new line."""

a = int(input("tell your number :- "))

while a > 0:
    print(a % 10)
    a = a // 10