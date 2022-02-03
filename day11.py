input_file = 'input11'

with open(input_file) as f:
    lines = f.readlines()

octopuses = [0]*len(lines)
for i in range(0, len(lines)):
    octopuses[i] =[int(l) for l in  lines[i].strip()]


def propagate_light(board, y, x):
    max_x = len(board[0])
    max_y = len(board)
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if (0 <= i < max_y and 0 <= j < max_x):
                
                board[i][j] += 1
                
                if board[i][j] == 10:
                    board = propagate_light(board, i, j) 
    return board
                

max_steps = 500
max_x = len(octopuses[0])
max_y = len(octopuses)
flash_counter = 0
for step in range(0, max_steps):
    #add 1 to all the values
    for i in range(0, max_y):
        for j in range(0, max_x):
            octopuses[i][j] += 1


    #make it flash 
    activated_octos = []
    for i in range(0, max_y):
        for j in range(0, max_x):
            if octopuses[i][j] == 10:
                activated_octos.append([i,j])

    for i in range(0, len(activated_octos)):
        octopuses = propagate_light(octopuses, activated_octos[i][0], activated_octos[i][1])

    flashes_step = 0
    #count flashes and set to 0 
    for i in range(0, max_y):
        for j in range(0, max_x):
            if octopuses[i][j] > 9:
                flashes_step += 1
                flash_counter += 1
                octopuses[i][j] = 0
    print('step ', step, 'flash_counter ', flash_counter)
    if flashes_step == max_x * max_y:
        print('step ', step + 1, ' all the octos are flashing')
