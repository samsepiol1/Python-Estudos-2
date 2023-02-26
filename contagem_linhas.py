count = 0

with open ('passlist.txt','r') as myfile:
    for line in myfile:
        count +=1
print(count)
