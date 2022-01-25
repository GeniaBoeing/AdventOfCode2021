import copy

input_file = 'input25'

with open(input_file) as f:
    board = f.readlines()
board = [list(i.strip()) for i in board]


def step(board):
    new_board = copy.deepcopy(board)
    nr_changes = 0
    #first east walking
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if j == len(board[0]) - 1: 
                neighbour = 0
            else:
                neighbour = j + 1
            if board[i][j] == '>' and board[i][neighbour] == '.':
                new_board[i][j] = '.'
                new_board[i][neighbour] = '>'

                nr_changes += 1 

    board = copy.deepcopy(new_board)
    #south 
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if i == len(board) - 1:
                neighbour = 0   
            else:
                neighbour = i + 1
            
            if board[i][j] == 'v' and board[neighbour][j] == '.':
                new_board[i][j] = '.'
                new_board[neighbour][j] = 'v'

                nr_changes += 1
    return new_board, nr_changes

nr_step = 0
moving = True
while(moving):
    print(nr_step)
    old_board = board
    board, nr_changes = step(board)
    nr_step += 1
    
    #check if equal
    if nr_changes == 0:
        moving = False

print('nr steps until not moving:   ', nr_step)
