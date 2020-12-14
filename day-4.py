
# Python3 code to demonstrate working of 
# Splitting text and number in string  
# Using re.compile() + re.match() + re.groups() 
import re

f = open("day-4-input.txt", "r")
lines = f.readlines()
f.close()

validCounter = 0

def passValidator(value):
    if len(value) == 9 and value.isdigit():
        return True
    else:
        return False

def eyeValidator(value):
    if value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth":
        return True
    else:
        return False

def numberValidator(value, min, max):

    return(min <= int(''.join(filter(str.isdigit, value))) <= max)
        

def colorValidator(strg):
    if(strg[0] == '#'):
        strg = strg.split('#')
        strg = strg[1]
        if(strg.isalnum()):
            if re.compile(r'[^a-f0-9.]').search:
                return True
            else:
                return False
        else:
            return False
    else:
            return False

def processLines(newLines):
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    
    for line in newLines:
        splitLine = line.split()
        for value in splitLine:
            p = value.split(':')
            if p[0] == "byr":
                byr = numberValidator(p[1], 1920, 2020)
            elif p[0] == "iyr":
                iyr = numberValidator(p[1], 2010, 2020)
            elif p[0] == "eyr":
                eyr = numberValidator(p[1], 2020, 2030)
            elif p[0] == "hgt":
                if "in" in p[1]:
                    hgt = numberValidator(p[1], 59, 76)
                elif "cm" in p[1]:
                    hgt = numberValidator(p[1], 150, 193)
            elif p[0] == "hcl":
                hcl = colorValidator(p[1])
            elif p[0] == "ecl":
                ecl = eyeValidator(p[1])
            elif p[0] == "pid":
                pid = passValidator(p[1])
    
    if(byr == False or iyr == False or eyr == False or hgt == False or hcl == False or ecl == False or pid == False):
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        return False
    else:
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        return True

for line in lines:
    if line != "\n":
        with open('test1.txt', 'a') as fout:
            fout.writelines(line)

    elif line == "\n":
        with open('test1.txt', 'r+') as fout:
            if processLines(fout.readlines()):
                validCounter += 1
            fout.truncate(0)

with open('test1.txt', 'a') as fout:
    fout.truncate(0)

print(validCounter)

