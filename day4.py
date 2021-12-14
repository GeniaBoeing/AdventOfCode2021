def check_if_bingo(rows, columns, board_size):
    #5 times same row|column within 5 rows|columns
    for i in range(0, len(rows)):
        #rows
        counter = 0
        for j in range(0, len(rows)):
            if rows[j] == rows[i]:
                counter += 1
        if counter == board_size:
            board_number = int(rows[i]/(board_size + 1))
            return [0, rows[i], board_number]

        #columns
        counter = 0
        for j in range(0, len(columns)):
            if columns[j] == columns[i] and int(rows[j]/(board_size + 1)) == int(rows[i]/(board_size + 1)):
                counter += 1
        if counter == board_size:
            board_number = int(rows[i]/(board_size + 1))
            return [1, columns[i], board_number]

    return [2]
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
for num in winning_nr:
    for line in range(0, len(bingo_boards)):
        if num in bingo_boards[line]:
            loc_in_line = 0
            for i in range(0, len(bingo_boards[line])):
                if bingo_boards[line][i] == num:
                    loc_in_line = i
            chosen_rows.append(line)
            chosen_columns.append(loc_in_line)
    result = check_if_bingo(chosen_rows, chosen_columns, board_size)
    if result[0] != 2:
        print(result)
        beginning = result[2] * (board_size + 1)
        end = beginning + board_size
        score = 0
        for line in range(beginning, end):
            if result[0] == 0:
                if line != result[1]:
                    score += sum(bingo_boards[line])
            if result[0] == 1:
                for i in range(0, board_size):
                    if i != result[1]:
                        print(bingo_boards[line])
                        score += bingo_boards[line][i]
        print(score * num)
        break
