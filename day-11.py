f = open("day-11-input.txt", "r")
lines = f.readlines()
f.close()

def checkAdjacentSeats(currentSeat, lines, i, j):
    b = 0
    if j == len(lines[i]) - 1:
        if i == len(lines) - 1:
            if currentSeat == 'L':
                if lines[i-1][j-1] == 'L' or lines[i-1][j-1] == '.':
                    b += 1
                if lines[i-1][j] == 'L' or lines[i-1][j] == '.':
                    b += 1
                if lines[i][j-1] == 'L' or lines[i][j-1] == '.':
                    b += 1
                if b == 3:
                    return True
                else:
                    return False

            elif currentSeat == '#':
                if lines[i-1][j-1] == '#':
                    b += 1
                if lines[i-1][j] == '#':
                    b += 1
                if lines[i][j-1] == '#':
                    b += 1
                if b >= 4:
                    return True
                else:
                    return False
        elif i == 0:
            if currentSeat == 'L':
                if lines[i][j-1] == 'L' or lines[i][j-1] == '.':
                    b += 1
                if lines[i+1][j-1] == 'L' or lines[i+1][j-1] == '.':
                    b += 1
                if lines[i+1][j] == 'L' or lines[i+1][j] == '.':
                    b += 1
                if b == 3:
                    return True
                else:
                    return False

            elif currentSeat == '#':
                if lines[i][j-1] == '#':
                    b += 1
                if lines[i+1][j-1] == '#':
                    b += 1
                if lines[i+1][j] == '#':
                    b += 1
                if b >= 4:
                    return True
                else:
                    return False
        else:
            if currentSeat == 'L':
                if lines[i-1][j-1] == 'L' or lines[i-1][j-1] == '.':
                    b += 1
                if lines[i-1][j] == 'L' or lines[i-1][j] == '.':
                    b += 1
                if lines[i][j-1] == 'L' or lines[i][j-1] == '.':
                    b += 1
                if lines[i+1][j-1] == 'L' or lines[i+1][j-1] == '.':
                    b += 1
                if lines[i+1][j] == 'L' or lines[i+1][j] == '.':
                    b += 1
                if b == 5:
                    return True
                else:
                    return False

            elif currentSeat == '#':
                if lines[i-1][j-1] == '#':
                    b += 1
                if lines[i-1][j] == '#':
                    b += 1
                if lines[i][j-1] == '#':
                    b += 1
                if lines[i+1][j-1] == '#':
                    b += 1
                if lines[i+1][j] == '#':
                    b += 1
                if b >= 4:
                    return True
                else:
                    return False
    elif j == 0:
        if i == len(lines) - 1:
            if currentSeat == 'L':
                if lines[i-1][j] == 'L' or lines[i-1][j] == '.':
                    b += 1
                if lines[i-1][j+1] == 'L' or lines[i-1][j+1] == '.':
                    b += 1
                if lines[i][j+1] == 'L' or lines[i][j+1] == '.':
                    b += 1
                if b == 3:
                    return True
                else:
                    return False

            elif currentSeat == '#':
                if lines[i-1][j] == '#':
                    b += 1
                if lines[i-1][j+1] == '#':
                    b += 1
                if lines[i][j+1] == '#':
                    b += 1
                if b >= 4:
                    return True
                else:
                    return False
        elif i == 0:
            if currentSeat == 'L':
                if lines[i][j+1] == 'L' or lines[i][j+1] == '.':
                    b += 1
                if lines[i+1][j] == 'L' or lines[i+1][j] == '.':
                    b += 1
                if lines[i+1][j+1] == 'L' or lines[i+1][j+1] == '.':
                    b += 1
                if b == 3:
                    return True
                else:
                    return False

            elif currentSeat == '#':
                if lines[i][j+1] == '#':
                    b += 1
                if lines[i+1][j] == '#':
                    b += 1
                if lines[i+1][j+1] == '#':
                    b += 1
                if b >= 4:
                    return True
                else:
                    return False
        else:
            if currentSeat == 'L':
                if lines[i-1][j] == 'L' or lines[i-1][j] == '.':
                    b += 1
                if lines[i-1][j+1] == 'L' or lines[i-1][j+1] == '.':
                    b += 1
                if lines[i][j+1] == 'L' or lines[i][j+1] == '.':
                    b += 1
                if lines[i+1][j] == 'L' or lines[i+1][j] == '.':
                    b += 1
                if lines[i+1][j+1] == 'L' or lines[i+1][j+1] == '.':
                    b += 1
                if b == 8:
                    return True
                else:
                    return False

            elif currentSeat == '#':
                if lines[i-1][j] == '#':
                    b += 1
                if lines[i-1][j+1] == '#':
                    b += 1
                if lines[i][j+1] == '#':
                    b += 1
                if lines[i+1][j] == '#':
                    b += 1
                if lines[i+1][j+1] == '#':
                    b += 1
                if b >= 4:
                    return True
                else:
                    return False
    else:
        if i == len(lines) - 1:
            if currentSeat == 'L':
                if lines[i-1][j-1] == 'L' or lines[i-1][j-1] == '.':
                    b += 1
                if lines[i-1][j] == 'L' or lines[i-1][j] == '.':
                    b += 1
                if lines[i-1][j+1] == 'L' or lines[i-1][j+1] == '.':
                    b += 1
                if lines[i][j-1] == 'L' or lines[i][j-1] == '.':
                    b += 1
                if lines[i][j+1] == 'L' or lines[i][j+1] == '.':
                    b += 1
                if b == 5:
                    return True
                else:
                    return False

            elif currentSeat == '#':
                if lines[i-1][j-1] == '#':
                    b += 1
                if lines[i-1][j] == '#':
                    b += 1
                if lines[i-1][j+1] == '#':
                    b += 1
                if lines[i][j-1] == '#':
                    b += 1
                if lines[i][j+1] == '#':
                    b += 1
                if b >= 4:
                    return True
                else:
                    return False
        elif i == 0:
            if currentSeat == 'L':
                if lines[i][j-1] == 'L' or lines[i][j-1] == '.':
                    b += 1
                if lines[i][j+1] == 'L' or lines[i][j+1] == '.':
                    b += 1
                if lines[i+1][j-1] == 'L' or lines[i+1][j-1] == '.':
                    b += 1
                if lines[i+1][j] == 'L' or lines[i+1][j] == '.':
                    b += 1
                if lines[i+1][j+1] == 'L' or lines[i+1][j+1] == '.':
                    b += 1
                if b == 5:
                    return True
                else:
                    return False

            elif currentSeat == '#':
                if lines[i][j-1] == '#':
                    b += 1
                if lines[i][j+1] == '#':
                    b += 1
                if lines[i+1][j-1] == '#':
                    b += 1
                if lines[i+1][j] == '#':
                    b += 1
                if lines[i+1][j+1] == '#':
                    b += 1
                if b >= 4:
                    return True
                else:
                    return False
        else:
            if currentSeat == 'L':
                if lines[i-1][j-1] == 'L' or lines[i-1][j-1] == '.':
                    b += 1
                if lines[i-1][j] == 'L' or lines[i-1][j] == '.':
                    b += 1
                if lines[i-1][j+1] == 'L' or lines[i-1][j+1] == '.':
                    b += 1
                if lines[i][j-1] == 'L' or lines[i][j-1] == '.':
                    b += 1
                if lines[i][j+1] == 'L' or lines[i][j+1] == '.':
                    b += 1
                if lines[i+1][j-1] == 'L' or lines[i+1][j-1] == '.':
                    b += 1
                if lines[i+1][j] == 'L' or lines[i+1][j] == '.':
                    b += 1
                if lines[i+1][j+1] == 'L' or lines[i+1][j+1] == '.':
                    b += 1
                if b == 8:
                    return True
                else:
                    return False

            elif currentSeat == '#':
                if lines[i-1][j-1] == '#':
                    b += 1
                if lines[i-1][j] == '#':
                    b += 1
                if lines[i-1][j+1] == '#':
                    b += 1
                if lines[i][j-1] == '#':
                    b += 1
                if lines[i][j+1] == '#':
                    b += 1
                if lines[i+1][j-1] == '#':
                    b += 1
                if lines[i+1][j] == '#':
                    b += 1
                if lines[i+1][j+1] == '#':
                    b += 1
                if b >= 4:
                    return True
                else:
                    return False
    return False
            
i = 0
j = 0

for line in lines:
    lines[i] = line.translate({ord(i): None for i in '\n'})
    i += 1

i = 0
sameCounter = 0
while sameCounter < 2:
    sameCounter = 0
    for line in lines:
        lineList = []
        print('line 1:', line)
        for x in line:
            #print(i)
            if x == 'L':
                if checkAdjacentSeats('L', lines, i, j):
                    x = '#'
            elif x == '#':
                if(checkAdjacentSeats('#', lines, i, j)):
                    x = 'L'      
            lineList.append(x)
            j += 1
        lines[i] = ''.join(lineList)
        print('Line 2:', lines[i])
        if line == lines[i]:
            sameCounter += 1

        #print('line 2:', ''.join(lineList))
        j = 0
        i += 1
    i = 0
    j = 0

counter = 0    
for line in lines:
    #print(line)
    for x in line:
        if x == '#':
            counter += 1
      
print('Counter:', counter)