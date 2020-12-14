f = open("day-11-input.txt", "r")
lines = f.readlines()
f.close()

for line in lines:
    for x in line:
        if x == 'L':
            x = '#'
        elif x == '#':
            