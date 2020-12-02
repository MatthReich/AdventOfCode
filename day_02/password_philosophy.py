import numpy as np

data = np.genfromtxt(fname="./puzzle_input.txt", dtype=str, delimiter=" ")


# part one
def calculate(datas):
    count = 0
    for x in datas:
        borders = x[0].split("-")
        num_min = int(borders[0])
        num_max = int(borders[1])
        requestedChar = x[1][0]
        sub_count = 0
        for char in x[2]:
            if char == requestedChar:
                sub_count += 1
        if num_min <= sub_count <= num_max:
            count += 1
    return count


print(calculate(data))


# part two
def calculatePartTwo(datas):
    count = 0
    for x in datas:
        borders = x[0].split("-")
        num_one = int(borders[0]) - 1
        num_two = int(borders[1]) - 1
        requestedChar = x[1][0]
        if len(x[2]) >= num_two:
            if bool(x[2][num_one] == requestedChar) != bool(x[2][num_two] == requestedChar):
                count += 1
    return count


print(calculatePartTwo(data))
