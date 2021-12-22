input_file = 'input13'
 
with open(input_file) as f:
    lines = f.readlines()

for l in range(0, len(lines)):
    if lines[l] == '\n':
        empty_line = l

dots = [lines[l].strip().split(',') for l in range(0, empty_line)]
dots = [[int(i) for i in l] for l in dots]

axis = {'y': 0, 'x': 1}
folds = [lines[l].strip() for l in range(empty_line+1, len(lines))]
#folds = [[axis[folds[l][-3]], int(folds[l][-1])] for l in range(0, len(folds))]
folds = [l.split(' ')[2].split('=') for l in folds]
folds = [[axis[l[0]], int(l[1])] for l in folds]

max_x = 0
max_y = 0
for dot in dots:
    if dot[0] > max_x: max_x = dot[0]
    
    if dot[1] > max_y: max_y = dot[1]

board = [0] * (max_y + 1)
board = [[0] * (max_x + 1) for i in board]
for dot in dots:
    board[dot[1]][dot[0]] = 1


def fold(axis, line):
    global max_x, max_y
    if axis == 0:
        max_y -= (line + 1)
    if axis == 1:
        max_x -= (line + 1)
    new_board = [0] * (max_y + 1)
    new_board = [[0] * (max_x + 1) for i in new_board]

    for i in range(0, max_y + 1):
        for j in range(0, max_x + 1):
            new_board[i][j] = board[i][j]
    if axis == 0:
        for i in range(max_y + 1, len(board)):
            for j in range(0, len(board[0])):
                y = i - abs(line - i) * 2
                if board[i][j] == 1:
                    new_board[y][j] = 1 

    if axis == 1:
        for i in range(0, len(board)):
            for j in range(max_x + 1, len(board[0])):
                x = abs(j - abs(line - j) * 2)
                if board[i][j] == 1:
                    new_board[i][x] = 1 
    return new_board

for f in folds:
    board = fold(f[0], f[1])
nr_dot = 0
for i in board:
    nr_dot += sum(i)

print('nr_dot after first fold : ', nr_dot)
for i in range(0, len(board)):
    for j in range(0, len(board[0])):
        if board[i][j] == 1:
            board[i][j] = '#'
        else:
            board[i][j] = '.'
for i in board:
    print(i)
