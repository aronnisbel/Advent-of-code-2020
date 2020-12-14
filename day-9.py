f = open("day-9-input.txt", "r")
lines = f.readlines()
f.close()

numbers = [None] * 25
i = 0
while i < 25:
    numbers[i] = lines[i]
    i += 1

def contains_sum(i):
    while True:
        for a in numbers:
            for b in numbers:
                if a != b:
                    #print(a, '+', b, '=', lines[i])
                    if (int(a) + int(b)) == int(lines[i]):
                        numbers.append(lines[i])
                        del numbers[0]
                        return True
        return False

while contains_sum(i):
    i += 1

j = 0
h = 0
sum = 0
contigousList = []
while True:
    sum += int(lines[j])
    if sum < int(lines[i]):
        contigousList.append(int(lines[j]))
        j += 1
    elif sum == int(lines[i]):
        sum = min(contigousList) + max(contigousList)
        break
    else:
        contigousList = []
        h += 1
        j = h
        sum = 0

        
print('Number: ', lines[i])
print('Sum: ', sum)