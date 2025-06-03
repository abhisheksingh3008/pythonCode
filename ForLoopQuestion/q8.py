"""Print all the factors of a number """

n = int(input("which number factors you want:-"))

for i in range(1,n+1):
    if n%i == 0:
        print(i)
