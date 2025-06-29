"""  Find the greatest element and print its index too. """

l = [12,36,14,18,128,6,13]

largest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f" Your largest number is {largest} at index {index}")