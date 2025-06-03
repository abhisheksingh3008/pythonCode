"""Factorial of a number """

n = int(input("Please tell your number : - "))

fact = 1

for i in range(1,n+1):
    fact = fact * i

print(f"Your factorial is {fact}")