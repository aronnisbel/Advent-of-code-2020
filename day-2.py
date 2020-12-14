f = open("day-2-input.txt", "r")
lines = f.readlines()
f.close()

splits = ""
numbers = []
criteria = ""
password = ""

counter = 0
counter2 = 0
legitcounter = 0

for line in lines:
    counter = 0
    splits = line.split()

    numbers = splits[0].split('-')
    criteria = splits[1].split(':')[0]
    password = splits[2]
    
    number1 = int(numbers[0])-1
    number2 = int(numbers[1])-1

    if (password[number1] == criteria) and (password[number2] != criteria):
        counter2 += 1
    elif (password[number1] != criteria) and (password[number2] == criteria):
        counter2 += 1
    else:
        print(numbers)
        print(number1, number2)
        print(password)
        print(password[number1]+" "+password[number2])
        print(criteria)
        print(line)

    for x in password:
        
        if x == criteria:
            counter += 1
    
    if int(numbers[0]) <= counter <= int(numbers[1]):
        legitcounter += 1

print(legitcounter)
print(counter2)