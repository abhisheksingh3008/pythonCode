"""  Count the frequency of each elements in a list """

a = [1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,7,7,7,7,8]
d = {}

for i in a:
    if i in d.keys():        # At a run time keys will be empty then code run the else statement
        d[i] += 1
    else:
        d[i] = 1

print(d) 



