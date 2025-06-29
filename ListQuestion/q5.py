"""  Check if List is sorted or not. """

l = [12,13,18,15,16]

for i in range(len(l)-1):
    if l[i] < l[i+1]:
        continue
    else:
        print(" your list is not sorted ")
        break
else:
    print(" your list is sorted ")
    
    
