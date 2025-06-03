"""Check wether the number is prime or not."""

n = int(input("Check wether the number is prime or not : "))

count = 0

for i in range(1,n+1):
    if n%i == 0:
        count = count + 1

if count == 2:
    print("Your number is Prime")

else:
    print("Your number is not prime")