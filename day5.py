input_file = 'input5'
with open(input_file) as f:
    file_line = f.readlines()
lines = []
for line in file_line:
    line = line.strip()
    line = line.split(' -> ')
    line = line[0].split(',' ) + line[1].split(',')
    line = [int(i) for i in line]
    lines.append(line)

#filter for horizontal/vertical lines

horizontal_lines = []
for line in lines:
    if line[1] == line[3]:
        horizontal_lines.append(line)

vertical_lines = []
for line in lines:
    if line[0] == line[2]:
        vertical_lines.append(line)

diagonal_lines = []
for line in lines:
    if line[0] != line[2] and line[1] != line[3]:
        diagonal_lines.append(line)

#Find maximum x and y values

max_x = 0
max_y = 0
for line in lines:
    if line[0] > max_x:
        max_x = line[0]
    if line[2] > max_x:
        max_x = line[2]
    
    if line[1] > max_y:
        max_y = line[1]
    if line[3] > max_y:
        max_y = line[3]

print('max x: ', max_x)
print('max y: ', max_y)

#set up matrix
board = [0]*(max_y + 1)
board = [[0]*(max_x + 1) for i in board]


for i in range(0, len(horizontal_lines)):
    if horizontal_lines[i][0] > horizontal_lines[i][2]:
        x_min = horizontal_lines[i][2]
        x_max = horizontal_lines[i][0]
    else:
        x_min = horizontal_lines[i][0]
        x_max = horizontal_lines[i][2]
        
    for j in range(x_min, x_max + 1):
        board[horizontal_lines[i][1]][j] += 1 


for i in range(0, len(vertical_lines)):
    if vertical_lines[i][1] > vertical_lines[i][3]:
        y_min = vertical_lines[i][3]
        y_max = vertical_lines[i][1]
    else:
        y_min = vertical_lines[i][1]
        y_max = vertical_lines[i][3]
        
    for j in range(y_min, y_max + 1):
        board[j][vertical_lines[i][0]] += 1 

for i in range(0, len(diagonal_lines)):
    if diagonal_lines[i][0] > diagonal_lines[i][2]:
        x_min = diagonal_lines[i][2]
        x_max = diagonal_lines[i][0]
    else: 
        x_min = diagonal_lines[i][0]
        x_max = diagonal_lines[i][2]


    if diagonal_lines[i][1] > diagonal_lines[i][3]:
        y_min = diagonal_lines[i][3]
        y_max = diagonal_lines[i][1]
    else:
        y_min = diagonal_lines[i][1]
        y_max = diagonal_lines[i][3]


    #which way does the diagonal lean?
    if (diagonal_lines[i][0] > diagonal_lines[i][2] and diagonal_lines[i][3] > diagonal_lines[i][1] or
        diagonal_lines[i][0] < diagonal_lines[i][2] and diagonal_lines[i][3] < diagonal_lines[i][1]): #left leaning 
        print(diagonal_lines[i])
        for k in range(0, y_max - y_min + 1):
            board[y_min + k][x_max - k] += 1
    else:
        for j in range(0, x_max - x_min + 1):
            board[y_min + j][x_min + j] += 1


#count how many tiles have a number larger equal to two

score = 0
for i in range(0, max_x + 1):
    for j in range(0, max_y + 1):
    
        if board[j][i] >= 2:
            score += 1

print('score:   ', score)


