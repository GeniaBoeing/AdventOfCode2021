input_file = '/Users/genia/Desktop/AdventOfCode2021/input2.txt'
direction = []
magnitude = []
with open(input_file) as f:
    for line in f:
        tmp = line.split()
        direction.append(str(tmp[0]))
        magnitude.append(int(tmp[1]))

x = 0 #horizontal position
y = 0 #depth

for i in range(0, len(direction)):
    if direction[i] == 'forward':
        x += magnitude[i]
    elif direction[i] == 'down':
        y += magnitude[i]
    elif direction[i] == 'up':
        y -= magnitude[i]
    else:
        print('uppsie : ', direction[i])

print('multiplying depth with horizontal position: ', x*y)


