f = open("day-10-input.txt", "r")
lines = f.readlines()
f.close()

i = 0
for line in lines:
    lines[i] = int(lines[i])
    i += 1
lines.sort()
print(lines)

ones = 0
threes = 0
i = 0
for line in lines:
    if i < len(lines)-1:
        if (lines[i+1] - line) == 1:
            ones += 1
        elif (lines[i+1] - line) == 3:
            threes += 1
    i += 1

memoize = [None] * 160
myset = set()

def adapter_search(myset, pv, i):
    if pv + 3 == 157:
        return pv
    
    if lines[i+1] - pv == 1:
        a = 1