import random
from pynput import keyboard


#fix problem with adding all the numbers in a column - needs to only add directly above/below
def print_matrix():
    for i in range(4):
        print(matrix[i])
    print("\n")


def add_two():
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    while matrix[x][y] != 0:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
    matrix[x][y] = 2


def down(row, col):
    sum = matrix[row][col]
    for i in range(row):
        if matrix[i][col] != 0:
            if matrix[i][col] == matrix[row][col] or matrix[i][col] == 0:
                sum += matrix[i][col]
                matrix[i][col] = 0

    matrix[row][col] = 0
    for i in range(4):
        if matrix[3 - i][col] == 0:
            matrix[3 - i][col] = sum
            break;


def move_down():
    for r in range(4):
        for c in range(4):
            if matrix[r][c] != 0:
                row = r
                col = c
                down(row, col);

    add_two()
    print_matrix()


def up(row, col):
    sum = matrix[row][col]
    for i in range (row):
        if matrix[i][col] != 0:
            if matrix[i][col] == matrix[row][col] or matrix[i][col] == 0:
                sum += matrix[i][col]
                matrix[i][col] = 0

    matrix[row][col] = 0
    for i in range(4):
        if matrix[i][col] == 0:
            matrix[i][col] = sum
            break;


def move_up():
    for r in range(4) :
        for c in range(4) :
            if matrix[r][c] != 0:
               row = r
               col = c
               up(row, col);

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





while(True):
    def on_press(key):
        if key == keyboard.Key.up:
            move_up()
            listener.stop();
        if key == keyboard.Key.down:
            move_down()
            listener.stop();
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()




