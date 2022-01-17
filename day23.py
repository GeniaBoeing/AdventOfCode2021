import numpy as np

amphipod_species = [1, 10, 100, 1000]

# Initialise the board
board = np.zeros((5, 11))
board[1,:] = [np.NAN, np.NAN, 3, np.NAN, 1, np.NAN, 4, np.NAN, 4, np.NAN, np.NAN]
board[2,:] = [np.NAN, np.NAN, 4, np.NAN, 3, np.NAN, 2, np.NAN, 1, np.NAN, np.NAN]
board[3,:] = [np.NAN, np.NAN, 4, np.NAN, 2, np.NAN, 1, np.NAN, 3, np.NAN, np.NAN]
board[4,:] = [np.NAN, np.NAN, 2, np.NAN, 1, np.NAN, 2, np.NAN, 3, np.NAN, np.NAN]

# winning_board
winning_board = board.copy()
winning_board[1:, 2] = [1, 1, 1, 1]
winning_board[1:, 4] = [2, 2, 2, 2]
winning_board[1:, 6] = [3, 3, 3, 3]
winning_board[1:, 8] = [4, 4, 4, 4]

def are_amphipods_settled(board):
    if np.array_equal(board, winning_board, equal_nan=True):
        return True
    return False


def move_amphipod(board, old_pos, new_pos):
    new_board = board.copy()
    new_board[old_pos[0], old_pos[1]] = 0
    new_board[new_pos[0], new_pos[1]] = board[old_pos[0], old_pos[1]]
    return new_board

def not_in_correct_space(board, pos):
    i = pos[1]
    j = pos[0]
    for k in range(4, j-1, -1):
        if board[k, i] != i/2: 
            return True
    return False


def possible_moves(board, score):
    next_boards = []
    # TODO: if score is bigger than my earlier attempt, abort. My weak heuristic. 46498. Thus the 2 hours attempting it by hand are not lost completely
    # moving from room through hallway to if possible room
    scores = []
    loitering_places = [i for i in range(0, len(board[0,:])) if board[0,i] == 0]
    for j in range(1, 5):
        for i in [2, 4, 6, 8]:
            if board[j, i] != 0 and board[j-1, i] == 0 and not_in_correct_space(board,[j, i]):
                score_multiplier = amphipod_species[int(board[j, i])-1]
                hallway_free = True
                pos = i 
                # going to the left
                while(hallway_free):
                    # check if right room and if can enter:
                    if pos in [2, 4, 6, 8] and board[j,i] == pos/2:
                        for k in range(4, 0, -1):
                            if board[k, pos] == 0:
                                scores.append((k + j + abs(pos - i)) * score_multiplier)
                                next_boards.append(move_amphipod(board, [j, i], [k, pos]))
                                break
                            elif board[k, pos] != pos - 1:
                                break
                    if (pos - 1) in loitering_places and pos in loitering_places:
                        scores.append((0 + j + abs(pos - 1 - i)) * score_multiplier)
                        next_boards.append(move_amphipod(board, [j, i], [0, pos-1])) 
                        if pos == 2: pos -= 1
                        else: pos -= 2
                    else: hallway_free = False  

                # going to the right 
                hallway_free = True
                pos = i 
                while(hallway_free):
                    if pos in [2, 4, 6, 8] and board[j,i] == pos/2:
                        for k in range(4, 0, -1):
                            if board[k, pos] == 0:
                                scores.append((k + j + abs(pos - i)) * score_multiplier)
                                next_boards.append(move_amphipod(board, [j, i], [k, pos]))
                                break
                            elif board[k, pos] != pos/2:
                                break
                    if (pos + 1) in loitering_places and pos in loitering_places:
                        scores.append((0 + j + abs(pos + 1 - i)) * score_multiplier)
                        next_boards.append(move_amphipod(board,[j, i], [0, pos+1]))
                        if pos == 8: pos += 1
                        else: pos += 2
                    else: hallway_free = False  
   
    
    # hallway to room possible? 
    j = 0
    for i in range(0, 11):
        if board[0, i] != 0:
            score_multiplier = amphipod_species[int(board[j, i])-1]
            hallway_free = True
            pos = i 
            # going to the left
            while(hallway_free):
                # check if right room and if can enter:
                if pos in [2, 4, 6, 8] and board[j,i] == pos/2:
                    for k in range(4, 0, -1):
                        if board[k, pos] == 0:
                            scores.append((k + j + abs(pos - i)) * score_multiplier)
                            next_boards.append(move_amphipod(board, [j, i], [k, pos]))
                            break
                        elif board[k, pos] != pos/2:
                            break
                # do not deposit in loitering_places but need to shove into room
                if (pos - 1) in loitering_places:
                    pos -= 1
                else: hallway_free = False 

            # going to the right 
            hallway_free = True
            pos = i 
            while(hallway_free):
                if pos in [2, 4, 6, 8] and board[j,i] == pos/2:
                    for k in range(4, 0, -1):
                        if board[k, pos] == 0:
                            scores.append((k + j + abs(pos - i)) * score_multiplier)
                            next_boards.append(move_amphipod(board, [j, i], [k, pos]))
                            break
                        elif board[k, pos] != pos/2:
                            break
                if (pos + 1) in loitering_places:
                    pos += 1
                else: hallway_free = False  
    scores = [ i + score for i in scores]
    return next_boards, scores
    



nearly_there = winning_board.copy()
nearly_there[0, 0] = 4
nearly_there[1, 2] = 0
nearly_there[2, 2] = 0
nearly_there[1, 4] = 2
nearly_there[1, 8] = 0
nearly_there[0, 9] = 1
nearly_there[0, 10] = 1

for i in nearly_there:
    print(i)

winning_scores = []

def step(board, score):
    global winning_scores
    next_boards, scores = possible_moves(board, score)
    for b in range(0, len(next_boards)):
        if are_amphipods_settled(next_boards[b]): 
            winning_scores.append(scores[b])
        elif scores[b] < 46498: #my weak ass heuristic
            step(next_boards[b], scores[b])

step(board, 0)
print('smalles winning score:   ', min(winning_scores))


            


    
