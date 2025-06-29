""" Mean of List elements. """

l = [12,34,54,3,15,29,64,9,13,7]

sum = 0

for i in l:
    sum = sum + i
    
print(sum/len(l))