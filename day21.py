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

input_file = 'ex21.txt'

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
    
