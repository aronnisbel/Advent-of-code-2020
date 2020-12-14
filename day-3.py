f = open("day-3-input.txt", "r")
lines = f.readlines()
f.close()

counter = 0
counter2 = 0
countertrees1 = 0
countertrees3 = 0
countertrees5 = 0
countertrees7 = 0
countertrees21 = 0
previousPos = 0

for line in lines:
    counter += 1
    if counter >= 2:
        condition = (counter - 1) * 3

        if condition <= 30:
            previousPos = condition
            if line[previousPos] == '#':
                countertrees3 += 1
                #print("Row:", counter, previousPos, "Yes")

        else:
            if previousPos < 28:
                previousPos = previousPos + 3
                if line[previousPos] == '#':
                        countertrees3 += 1
                        
            else:
                if previousPos == 28:
                    previousPos = 0

                elif previousPos == 29:
                    previousPos = 1

                else:
                    previousPos = 2

                if line[previousPos] == '#':
                    countertrees3 += 1

#########################################################
counter = 0
previousPos = 0
for line in lines:
    counter += 1
    if counter >= 2:
        condition = (counter - 1)

        if condition <= 30:
            previousPos = condition
            if line[previousPos] == '#':
                countertrees1 += 1
                #print("Row:", counter, previousPos, "Yes")

        else:
            if previousPos < 30:
                previousPos = previousPos + 1
                if line[previousPos] == '#':
                        countertrees1 += 1
                        
            else:
                if previousPos == 30:
                    previousPos = 0

                if line[previousPos] == '#':
                    countertrees1 += 1

############################################################
counter = 0
previousPos = 0
for line in lines:
    counter += 1
    if counter >= 2:
        condition = (counter - 1) * 5

        if condition <= 30:
            previousPos = condition
            if line[previousPos] == '#':
                countertrees5 += 1
                #print("Row:", counter, previousPos, "Yes")

        else:
            if previousPos < 26:
                previousPos = previousPos + 5
                if line[previousPos] == '#':
                        countertrees5 += 1
                        
            else:
                if previousPos == 26:
                    previousPos = 0
                elif previousPos == 27:
                    previousPos = 1
                elif previousPos == 28:
                    previousPos = 2
                elif previousPos == 29:
                    previousPos = 3
                elif previousPos == 30:
                    previousPos = 4

                if line[previousPos] == '#':
                    countertrees5 += 1

###########################################

counter = 0
previousPos = 0
for line in lines:
    counter += 1
    if counter >= 2:
        condition = (counter - 1) * 7

        if condition <= 30:
            previousPos = condition
            if line[previousPos] == '#':
                countertrees7 += 1
                #print("Row:", counter, "condition", condition, previousPos, "Yes condition 1")

        else:
            if previousPos < 24:
                previousPos = previousPos + 7
                if line[previousPos] == '#':
                        countertrees7 += 1
                        #print("Row:", counter, previousPos, "Yes < 24")

                        
            else:
                if previousPos == 24:
                    previousPos = 0
                elif previousPos == 25:
                    previousPos = 1
                elif previousPos == 26:
                    previousPos = 2
                elif previousPos == 27:
                    previousPos = 3
                elif previousPos == 28:
                    previousPos = 4
                elif previousPos == 29:
                    previousPos = 5
                elif previousPos == 30:
                    previousPos = 6

                if line[previousPos] == '#':
                    countertrees7 += 1
                    #print("Row:", counter, previousPos, "Yes else")


#############################################################

counter = 0
previousPos = 0
for line in lines:
    counter += 1
    if counter > 2 and ((counter % 2) != 0):

        if counter <= 30:
            previousPos += 1
            if line[previousPos] == '#':
                countertrees21 += 1
                #print("Row:", counter, previousPos, "Yes")

        else:
            if previousPos < 30:
                previousPos = previousPos + 1
                if line[previousPos] == '#':
                        countertrees21 += 1
                        
            else:
                #print("pP", previousPos)
                if previousPos == 30:
                    previousPos = 0

                if line[previousPos] == '#':
                    countertrees21 += 1


print("Trees 1:", countertrees1)
print("Trees 3:", countertrees3)
print("Trees 5:", countertrees5)
print("Trees 7:", countertrees7)
print("Trees 21:", countertrees21)

print(countertrees1*countertrees21*countertrees3*countertrees5*countertrees7)