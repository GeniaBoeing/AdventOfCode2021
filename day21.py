import numpy as np

def get_player_pos(line):
    player = [i for i in line if i in '1234567890']
    player = player[1:]
    pos = ''
    for i in player:
        pos += i
    return int(pos)

def get_new_position(old, add):
    pos = old + add
    pos = pos % 10 
    if pos == 0:
        pos = 10
    return pos

input_file = 'input21'

with open(input_file) as f:
    lines = f.readlines()

player1 = get_player_pos(lines[0])
player2 = get_player_pos(lines[1])
print('position of players: ', player1, player2)

def deterministic_die(last_add):
    value = 0
    for i in range(3):
        last_add += 1
        value += last_add
        if last_add == 100: last_add = 0
    return value, last_add

not_finished_game = True
score_1 = 0
score_2 = 0
last_add = 0
die_rolls = 0
result = 0
while(not_finished_game):
    value, last_add = deterministic_die(last_add)
    die_rolls += 3
    player1 = get_new_position(player1, value)
    score_1 += player1 
    if score_1 >= 1000: 
        not_finished_game = False
        result = score_2 * die_rolls
        break
    value, last_add = deterministic_die(last_add)   
    die_rolls += 3
    player2 = get_new_position(player2, value)
    score_2 += player2 
    if score_2 >= 1000: 
        not_finished_game = False
        result = score_1 * die_rolls
        break
print('result:  ', result)
   

#### part 2: Dirac Dice 

scores_prob = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]

def mod10(n):
    while(n > 10):
        n -= 10
    return n

def update_universes(universes):
    for player in range(2):
        universes_old = universes.copy()
        for p1_score in range(0, 21):
            for p1_pos in range(1, 11):
                for p2_score in range(0, 21):
                    for p2_pos in range(1, 11):
                        for roll in range(3, 10):
                            roll_p = scores_prob[roll]
                            if player == 0:
                                new_pos = mod10(p1_pos + roll)
                                new_score = p1_score + new_pos
                                if new_score > 21: new_score = 21
                                universes[new_score][new_pos][p2_score][p2_pos] += roll_p * universes_old[p1_score][p1_pos][p2_score][p2_pos]
                            else:
                                new_pos = mod10(p2_pos + roll)
                                new_score = p2_score + new_pos
                                if new_score > 21: new_score = 21
                                universes[p1_score][p1_pos][new_score][new_pos] += roll_p * universes_old[p1_score][p1_pos][p2_score][p2_pos]
                        universes[p1_score][p1_pos][p2_score][p2_pos] -= universes_old[p1_score][p1_pos][p2_score][p2_pos]
    return universes

def every_universe_has_winner(universes):

    for p1_score in range(0, 21):
        for p1_pos in range(1, 11):
            for p2_score in range(0, 21):
                for p2_pos in range(1, 11):
                    if universes[p1_score][p1_pos][p2_score][p2_pos] > 0:
                        return False

    return True

def nr_wins(universes):
    p1_wins = 0
    p2_wins = 0
    for p1_pos in range(1, 11):
        for p2_score in range(0, 21):   
            for p2_pos in range(1, 11):
               p1_wins += universes[21][p1_pos][p2_score][p2_pos]
 
    for p1_score in range(0, 21):
        for p1_pos in range(1, 11):
            for p2_pos in range(1, 11):
               p2_wins += universes[p1_score][p1_pos][21][p2_pos]
    return p1_wins, p2_wins


player1 = get_player_pos(lines[0])
player2 = get_player_pos(lines[1])
print('position of players: ', player1, player2)
universes = np.zeros((22, 11, 22, 11), dtype = int)
universes[0][player1][0][player2] = 1

i = 0
while(not every_universe_has_winner(universes)):
    universes = update_universes(universes)
    p1_wins, p2_wins = nr_wins(universes)
    print(i)
    i += 1
    print('player 1 wins in ', p1_wins, ' universes and player 2 in ', p2_wins)



 
