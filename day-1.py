f = open("day-1-input.txt", "r")
lines = f.readlines()
f.close()
a = 0
b = 0

for number in lines:
    for number2 in lines:
        for number3 in lines:
            if (int(number) + int(number2) + int(number3)) == 2020:
                a = int(number)
                b = int(number2)
                c = int(number3)
                print(a)
                print(b)
                print(c)
                print(a * b * c)
                break