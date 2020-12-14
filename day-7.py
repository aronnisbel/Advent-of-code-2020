f = open("control-input.txt", "r")
lines = f.readlines()
f.close()

bags1 = []
first2bags = []
myset = set()
amount = 0

def findBags(bag):
    myset = set()
    number = 0
    multiplier = 0
    for line in lines:
        line = line.replace('bags', '')
        line = line.replace('bag', '')
        line = line.translate({ord(i): None for i in ' \n.'})
        bags1 = line.split(',')
        first2bags = bags1[0].split('contain')
        del bags1[0]          
        if(first2bags[0] == bag):
            myset.add(first2bags[1])
            for bag in bags1:
                myset.add(bag)
    if len(myset) != 0:
        for bag in myset:
            if bag[0].isdigit():
                multiplier = int(bag[0])
            number += multiplier + (multiplier * findBags(''.join([i for i in bag if not i.isdigit()])))
            print(number)
    return number

amount = findBags('shinygold')
print("Amount:",amount)