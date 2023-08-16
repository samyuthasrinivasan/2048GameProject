import random
from pynput import keyboard

# need to fix this error

# [2, 2, 2, 2]
# [8, 4, 4, 4]
# [4, 2, 2, 2]
# [0, 0, 0, 2]
#
# [0, 2, 0, 0]
# [2, 2, 2, 0]
# [8, 4, 4, 2]
# [4, 2, 2, 8]

# jumps a step by adding the 4 from the added 2s to the nearby 4
# check if its a sum, if not add it, if it is leave it be

def print_matrix():
    for j in range(4):
        print(matrix[j])
    print("\n")


def add_two( ):
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

def move_left(row, col):
    sum = matrix[row][col]

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
            move_left(1, 1)
            listener.stop()
        if key == keyboard.Key.right:
            move_right(1, 1)
            listener.stop()
        if key == keyboard.Key.esc:
            listener.stop()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()




