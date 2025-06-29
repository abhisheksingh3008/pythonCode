""" Write a Python script to merge two Python dictionaries """

d1 = {10:100,20:200,30:300}
d2 = {40:400,50:500,60:600}

for i in d2:
    d1[i] = d2[i]

print(d1)

# if two same key belong to different dictionary

d1 = {10:100,20:200,40:300}
d2 = {40:400,50:500,60:600}

for i in d2:
    d1[i] = d2[i]

print(d1)