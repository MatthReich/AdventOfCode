f = open('./puzzle_input.txt')
data = [line.replace('\n', '') for line in f]


# part one
def calculate(datas):
    trees = 0
    for i in range(len(datas)):
        sub_trees = 0
        right = 3
        down = 1
        position_x = 0

        for position_y in range(0, len(datas), down):
            if datas[position_y][position_x] == "#":
                sub_trees += 1
            position_x = (position_x + right) % len(datas[0])
        trees = sub_trees
    return trees


print(calculate(data))


# part two
def calculate_two(datas):
    list_right = [1, 3, 5, 7, 1]
    list_down = [1, 1, 1, 1, 2]
    allSlopes = 1
    for i in range(len(list_right)):
        sub_trees = 0
        right = list_right[i]
        down = list_down[i]
        position_x = 0

        for position_y in range(0, len(datas), down):
            if datas[position_y][position_x] == "#":
                sub_trees += 1
            position_x = (position_x + right) % len(datas[0])
        allSlopes *= sub_trees
    return allSlopes


print(calculate_two(data))
