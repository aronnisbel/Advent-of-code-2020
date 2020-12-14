import math

f = open("day-5-input.txt", "r")
lines = f.readlines()
f.close()

maxValue = 0
row = 0
column = 0
seatMap = [[0 for i in range(8)] for j in range(127)] 
seatIDs = []

for line in lines:

    rows = []
    for i in range(128):
        rows.append(i)

    columns = []
    for i in range(8):
        columns.append(i)

    for x in line:
        if x == 'F':
            if len(rows) > 2:
                a = rows[0]
                b = rows[round(len(rows)/2)-1]
                rows.clear()
                rows = []
                for i in range(a, b+1):
                    rows.append(i)
            else:
                row = rows[0]

        elif x == 'B':
            if len(rows) > 2:
                a = rows[round(len(rows)/2)]
                b = rows[len(rows)-1]
                rows.clear()
                rows = []
                for i in range(a, b+1):
                    rows.append(i)
            else:
                row = rows[1]

        elif x == 'L':
            if len(columns) > 2:
                a = columns[0]
                b = columns[round(len(columns)/2)-1]
                if a != b:
                    columns.clear()
                    columns = []
                    for i in range(a, b+1):
                        columns.append(i)
            else:
                #print(columns, "L")
                column = columns[0]

        elif x == 'R':
            if len(columns) > 2:
                a = columns[round(len(columns)/2)]
                b = columns[len(columns)-1]
                #print(len(columns))
                if a != b:
                    columns.clear()
                    columns = []
                    #print(a,b)
                    for i in range(a, b+1):
                        columns.append(i)
            else:
                #print(columns, "R")
                column = columns[1]

    newValue = (row * 8) + column
    seatIDs.append(newValue)
    
    #print(column, row)

    if(newValue > maxValue):
        maxValue = newValue
    
    seatMap[row][column] = 1

seatIDs.sort()
#print(seatIDs)

seats = 0
for row in seatMap:
    print("Row", seats, row)
    seats += 1


print("Max value is:", maxValue)
