import numpy as np

data = np.genfromtxt(fname="./puzzle_input.txt", dtype=int, delimiter=" ")


# part one
def calculate_two(numbers):
    for x in numbers:
        for y in numbers[1:]:
            if x + y == 2020:
                return x, y


pair = calculate_two(data)
result = pair[0] * pair[1]
print("number 1: " + str(pair[0]) + ", number 2: " + str(pair[1]) + " = " + str(result))


# part two
def calculate_three(numbers):
    for x in numbers:
        for y in numbers[1:]:
            for z in numbers[2:]:
                if x + y + z == 2020:
                    return x, y, z


pair = calculate_three(data)
result = pair[0] * pair[1] * pair[2]
print("number 1: " + str(pair[0]) + ", number 2: " + str(pair[1]) + ", number 3: " + str(pair[2]) + " = " + str(result))
