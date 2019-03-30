def apply_right(line, column, numbers):
    prod = 1
    if(column>16):
        return 0
    else:
        for i in range(0,4):
            prod*=numbers[line][column+i]
    return prod

def apply_down(line, column, numbers):
    prod = 1
    if(line>16):
        return 0
    else:
        for i in range(0,4):
            prod*=numbers[line+i][column]
    return prod

def apply_diago_right(line, column, numbers):
    prod = 1
    if(line>16 or column>16):
        return 0
    else:
        for i in range(0,4):
            prod*=numbers[line+i][column+i]
    return prod

def apply_diago_left(line, column, numbers):
    prod = 1
    if(line>16 or column<3):
        return 0
    else:
        for i in range(0,4):
            prod*=numbers[line+i][column-i]
    return prod


f = open("P011.txt", "r")
flines = f.readlines()
i = 0
max = 0
tmp = 0
numbers = []
for line in flines:
    numbers.append([int(x) for x in line.split()])
    i+=1
for line in range(0,20):
    for column in range(0,20):
        tmp = apply_down(line, column, numbers)
        if(tmp>max):
            max = tmp
        tmp = apply_right(line, column, numbers)
        if(tmp>max):
            max = tmp
        tmp = apply_diago_left(line, column, numbers)
        if(tmp>max):
            max = tmp
        tmp = apply_diago_right(line, column, numbers)
        if(tmp>max):
            max = tmp
print(max)
