def check_if_bingo(rows, columns, board_size):
    #5 times same row|column within 5 rows|columns
    winning_boards = []

    for i in range(0, len(rows)):
        #rows
        counter = 0
        for j in range(0, len(rows)):
            if rows[j] == rows[i]:
                counter += 1
        board_number = int(rows[i]/(board_size + 1))
        if counter == board_size and board_number not in winning_boards:
            winning_boards.append(board_number)

        #columns
        counter = 0
        for j in range(0, len(rows)):
            if columns[j] == columns[i] and int(rows[j]/(board_size + 1)) == int(rows[i]/(board_size + 1)):
                counter += 1
        board_number = int(rows[i]/(board_size + 1))
        if counter == board_size and board_number not in winning_boards:
            winning_boards.append(board_number)
    return winning_boards



input_file = 'input4.txt'

with open(input_file) as f:
    lines = f.readlines()
board_size = 5


winning_nr = lines[0][:-1].split(',')
winning_nr = [int(i) for i in winning_nr]

bingo_boards = lines[2:]
bingo_boards = [i.split() for i in bingo_boards]
bingo_boards = [[int(j) for j in i] for i in bingo_boards]

#winning_nr = [7, 42, 22, 92, 60]
#winning_nr = [7, 86, 50, 78, 16]
#winning_nr = [86, 45, 98, 19, 51]
chosen_rows = []
chosen_columns = []
chosen_num = []
winning_boards = []
for num in winning_nr:
    print(num)
    for line in range(0, len(bingo_boards)):
        if num in bingo_boards[line]:
            loc_in_line = 0
            for i in range(0, len(bingo_boards[line])):
                if bingo_boards[line][i] == num:
                    loc_in_line = i
            chosen_rows.append(line)
            chosen_columns.append(loc_in_line)
            chosen_num.append(num)
        
    winning_boards.append(check_if_bingo(chosen_rows, chosen_columns, board_size))

for i in range(len(winning_boards)-1, -1, -1):
    if len(winning_boards[i]) != len(winning_boards[i-1]):
        print(winning_boards[i])
        print(winning_boards[i-1])
        last_winning_board = [j for j in winning_boards[i] if j not in winning_boards[i-1]]
        break    


last_board = last_winning_board[0]
last_beginning = last_board * (board_size + 1)
last_end = last_beginning + board_size
last_indexes = [i for i in range(0, len(chosen_rows)) if chosen_rows[i] >= last_beginning and chosen_rows[i] < last_end]
last_rows = [chosen_rows[i] for i in last_indexes]
last_columns = [chosen_columns[i] for i in last_indexes]
last_chosen_num = [chosen_num[i] for i in last_indexes]
winning_boards = []
score = 0
for i in range(0, len(last_rows)):
    result = check_if_bingo(last_rows[:i+1], last_columns[:i+1], board_size)
    if result:
        for line in range(last_beginning, last_end):
            score += sum(bingo_boards[line])
        for i in range(0, len(last_rows[:i+1])):
            score -= bingo_boards[last_rows[i]][last_columns[i]]
        print('score ', score, '    winning num: ', last_chosen_num[i], 'thus final score is: ', score * last_chosen_num[i])
        break

