"""Take a number as input and print its table """

n = int(input("Which table you want : - "))

for i in range(1,11):
    print(f"{n} * {1} = {n*i}")