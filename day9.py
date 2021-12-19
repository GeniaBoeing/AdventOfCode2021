input_file = 'input9'

with open(input_file) as f:
    lines = f.readlines()
board = [0] * len(lines)
for l in range(0, len(lines)):
    board[l] = [int(i) for i in lines[l].strip()]
max_y = len(board)
max_x = len(board[0])
print('max x and max y', max_x, max_y) 

#middle part:
counter = 0
low_points = []
for i in range(1, max_y - 1):
    for j in range(1, max_x - 1):
        if (board[i][j] < board[i][j-1] and
            board[i][j] < board[i][j+1] and
            board[i][j] < board[i-1][j] and
            board[i][j] < board[i+1][j]):
            counter += 1 + board[i][j]
            low_points.append([i, j])
#edges:
for j in range(1, max_x - 1):
    
    #upper edge
    if (board[0][j] < board[0][j-1] and
        board[0][j] < board[0][j+1] and
        board[0][j] < board[1][j]):
        counter += 1 + board[0][j]
        low_points.append([0, j])
    #lower edge
    if (board[max_y-1][j] < board[max_y-1][j-1] and
        board[max_y-1][j] < board[max_y-1][j+1] and
        board[max_y-1][j] < board[max_y-2][j]):
        counter += 1 + board[max_y-1][j]
        low_points.append([max_y-1, j])
for j in range(1, max_y - 1):
    
    #left edge:
    if (board[j][0] < board[j-1][0] and 
        board[j][0] < board[j+1][0] and
        board[j][0] < board[j][1]):
        counter += 1 + board[j][0]
        low_points.append([j, 0])
    #right edge:
    
    if (board[j][max_x-1] < board[j-1][max_x-1] and 
        board[j][max_x-1] < board[j+1][max_x-1] and
        board[j][max_x-1] < board[j][max_x-2]):
        counter += 1 + board[j][max_x-1]
        low_points.append([j, max_x-1])
#corners

if board[0][0] < board[0][1] and board[0][0] < board[1][0]: 
    counter += 1 + board[0][0]
    low_points.append([0, 0])
if board[0][max_x-1] < board[0][max_x-2] and board[0][max_x-1] < board[1][max_x-1]: 
    counter += 1 + board[0][max_x-1]
    low_points.append([0, max_x-1])
if board[max_y-1][0] < board[max_y-1][1] and board[max_y-1][0] < board[max_y-2][0]: 
    counter += 1 + board[max_y-1][0]
    low_points.append([max_y-1, 0])
if board[max_y-1][max_x-1] < board[max_y-1][max_x-2] and board[max_y-1][max_x-1] < board[max_y-2][max_x-1]: 
    counter += 1 + board[max_y-1][max_x-1]
    low_points.append([max_y-1, max_x-1])


print('counter: ', counter)

#Part 2: find 3 largest basins
def basin_neighbours(board, y, x, basin_size):
    #up
    if y - 1 >= 0:
        if board[y-1][x] == 0:
            basin_size += 1
            board[y-1][x] = 1
            board, basin_size = basin_neighbours(board, y-1, x, basin_size)
    #down
    if y + 1 < len(board):
        if board[y+1][x] == 0:
            basin_size += 1
            board[y+1][x] = 1
            board, basin_size = basin_neighbours(board, y+1, x, basin_size)
    #left
    if x - 1 >= 0:
        if board[y][x-1] == 0:
            basin_size += 1
            board[y][x-1] = 1
            board, basin_size = basin_neighbours(board, y, x-1, basin_size)
    if x + 1 < len(board[0]):
        if board[y][x+1] == 0:
            basin_size += 1
            board[y][x+1] = 1
            board, basin_size = basin_neighbours(board, y, x+1, basin_size)
    
    return board, basin_size
basin_size = [0] * len(low_points)
for i in range(0, max_y):
    for j in range(0, max_x):
        if board[i][j] != 9:
            board[i][j] = 0

for i in range(0, len(low_points)):
    board, basin_size[i] = basin_neighbours(board, low_points[i][0], low_points[i][1], basin_size[i])

basin_size.sort(reverse=True)
print('largest three basin sizes multiplied:    ', basin_size[0]*basin_size[1]*basin_size[2])
           









