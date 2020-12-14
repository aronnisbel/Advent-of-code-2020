import re

f = open("day-6-input.txt", "r")
lines = f.readlines()
f.close()

previousset = set()
newset = set()
yesSum = 0

for line in lines:
    if line != '\n':
        if len(previousset) == 0:
            for x in line:
                if x != '\n' and x.isalpha():
                    previousset.add(x)
        else:
            for x in line:
                if x != '\n' and x.isalpha():
                    if x in previousset:
                        newset.add(x)
            
            if len(newset) != 0:
                previousset = newset
                newset = set()
            else:
                previousset = set('1')
                
    elif line == '\n':
        #print(myset)
        if('1' in previousset):
            previousset = set()

        yesSum += len(previousset)
        previousset = set()
        newset = set()

yesSum += len(previousset)
print(yesSum)
