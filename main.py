import random
from pynput import keyboard


def print_matrix():
    for j in range(4):
        print(matrix[j])
    print("\n")


def add_two():
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    while matrix[x][y] != 0:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    matrix[x][y] = 2


def set_below(row, col):
    below = 0
    while below == 0 and row < 3:
        below = matrix[row + 1][col]
        row += 1
    return row


def set_left(row, col):
    left = 0
    while left == 0 and col > 0:
        left = matrix[row][col - 1]
        col -= 1
    return col


def set_right(row, col):
    right = 0
    while right == 0 and col < 3:
        right = matrix[row][col + 1]
        col += 1
    return col


def set_above(row, col):
    above = 0
    while above == 0 and row > 0:
        above = matrix[row - 1][col]
        row -= 1
    return row


def down(row, col):
    point = matrix[row][col]
    sum = point
    below = 0
    above = 0

    if row == 0:
        selected_row_below = set_below(row, col)
        below = matrix[selected_row_below][col]
        above = 1

    if row == 3:
        selected_row_above = set_above(row, col)
        above = matrix[selected_row_above][col]
        below = 1

    if row > 0 and row < 3:
        selected_row_above = set_above(row, col)
        selected_row_below = set_below(row, col)
        above = matrix[selected_row_above][col]
        below = matrix[selected_row_below][col]

    if below == point:
        sum += below
        matrix[row][col] = 0
        matrix[selected_row_below][col] = 0

    else:
        if above == point:
            sum += above
            matrix[row][col] = 0
            matrix[selected_row_above][col] = 0

        else:
            matrix[row][col] = 0


    iteratorRow = row
    pointRow = row
    while matrix[iteratorRow][col] == 0 & iteratorRow < 4:
        pointRow = iteratorRow
        iteratorRow += 1
        if iteratorRow == 4:
            break

    matrix[pointRow][col] = sum


def move_down():

    for r in range(4):
        for c in range(4):
            if matrix[3 - r][3 - c] != 0:
                row = 3 - r
                col = 3 - c
                down(row, col)

    add_two()
    print_matrix()


def up(row, col):
    point = matrix[row][col]
    sum = point
    below = 0
    above = 0

    if row == 0:
        selected_row_below = set_below(row, col)
        below = matrix[selected_row_below][col]
        above = 1

    if row == 3:
        selected_row_above = set_above(row, col)
        above = matrix[selected_row_above][col]
        below = 1

    if row > 0 and row < 3:
        selected_row_above = set_above(row, col)
        selected_row_below = set_below(row, col)
        above = matrix[selected_row_above][col]
        below = matrix[selected_row_below][col]

    if above == point:
        sum += above
        matrix[row][col] = 0
        matrix[selected_row_above][col] = 0

    else:
        if below == point:
            sum += below
            matrix[row][col] = 0
            matrix[selected_row_below][col] = 0

        else:
            matrix[row][col] = 0

    iteratorRow = row
    pointRow = row
    while matrix[iteratorRow][col] == 0 & iteratorRow > -1:
        pointRow = iteratorRow
        iteratorRow -= 1
        if iteratorRow == -1:
            break

    matrix[pointRow][col] = sum


def move_up():
    for r in range(4) :
        for c in range(4) :
            if matrix[r][c] != 0:
               row = r
               col = c
               up(row, col)

    add_two()
    print_matrix()

def move_right(row, col):
    sum = matrix[row][col]


def left(row, col):
    point = matrix[row][col]
    sum = point
    right_side = 0
    left_side = 0

    if col == 0:
        selected_right = set_right(row, col)
        right_side = matrix[row][selected_right]
        left_side = 1

    if col == 3:
        selected_left = set_left(row, col)
        left_side = matrix[row][selected_left]
        right_side = 1

    if col > 0 and col < 3:
        selected_left = set_left(row, col)
        selected_right = set_right(row, col)
        left_side = matrix[row][selected_left]
        right_side = matrix[row][selected_right]

    if left_side == point:
        sum += left_side
        matrix[row][col] = 0
        matrix[selected_left][col] = 0

    else:
        if right_side == point:
            sum += right_side
            matrix[row][col] = 0
            matrix[row][selected_right] = 0

        else:
            matrix[row][col] = 0

    iteratorCol = col
    pointCol = col
    while matrix[row][iteratorCol] == 0 & iteratorCol > -1:
        pointCol = iteratorCol
        iteratorCol -= 1
        if iteratorCol == -1:
            break

    matrix[row][pointCol] = sum


def move_left():
    for r in range(4) :
        for c in range(4) :
            if matrix[r][c] != 0:
               row = r
               col = c
               left(row, col)

    add_two()
    print_matrix()


def right(row, col):
    point = matrix[row][col]
    sum = point
    right_side = 0
    left_side = 0

    if col == 0:
        selected_right = set_right(row, col)
        right_side = matrix[row][selected_right]
        left_side = 1

    if col == 3:
        selected_left = set_left(row, col)
        left_side = matrix[row][selected_left]
        right_side = 1

    if col > 0 and col < 3:
        selected_left = set_left(row, col)
        selected_right = set_right(row, col)
        left_side = matrix[row][selected_left]
        right_side = matrix[row][selected_right]

    if right_side == point:
        sum += right_side
        matrix[row][col] = 0
        matrix[row][selected_right] = 0

    else:
        if left_side == point:
            sum += left_side
            matrix[row][col] = 0
            matrix[row][selected_left] = 0

        else:
            matrix[row][col] = 0


    iteratorCol = col
    pointCol = col
    while matrix[row][iteratorCol] == 0 & iteratorCol < 4:
        pointCol = iteratorCol
        iteratorCol += 1
        if iteratorCol == 4:
            break

    matrix[row][pointCol] = sum


def move_right():

    for r in range(4):
        for c in range(4):
            if matrix[3 - r][3 - c] != 0:
                row = 3 - r
                col = 3 - c
                right(row, col)

    add_two()
    print_matrix()


print("2048!")
matrix = []
for i in range(4):
    matrix.append([0] * 4)

x = random.randint(0, 3)

y = random.randint(0, 3)
matrix[y][x] = 2
print_matrix()


while True:
    def on_press(key):
        if key == keyboard.Key.up:
            move_up()
            listener.stop()
        if key == keyboard.Key.down:
            move_down()
            listener.stop()
        if key == keyboard.Key.left:
            move_left()
            listener.stop()
        if key == keyboard.Key.right:
            move_right()
            listener.stop()
        if key == keyboard.Key.esc:
            listener.stop()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()





