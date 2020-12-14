f = open("day-8-input.txt", "r")
lines = f.readlines()
f.close()

def boot_program(elements):

    acc = 0
    i = 0
    myset = set()
    #print(elements)

    while True:

        if i == len(elements):
            print('Right acc', acc)
            return acc

        values = elements[i].split()
        values[1] = values[1].translate({ord(i): None for i in '\n'})

        if values[0] == 'acc':
            acc += int(values[1])
            i += 1
            if i in myset:
                break
        
        elif values[0] == 'jmp':
            if int(values[1]) == 0:
                break            
            i += int(values[1])
            if i in myset:
                break
        
        elif values[0] == 'nop':
            i += 1
            if i in myset:
                break

        myset.add(i)
    return acc

#Length 596
accelerator = 0
i = 0
myset = set()

for line in lines:
    values = lines[i].split()
    if values[0] == 'jmp':
        elements = lines.copy()
        elements[i] = 'nop ' + values[1]
        accelerator = boot_program(elements)

    elif values[0] == 'nop':
        elements = lines.copy()
        elements[i] = 'jmp ' + values[1]
        accelerator = boot_program(elements)

    i += 1

print('Next i:',i)
print('acc:',accelerator)
