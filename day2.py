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

print('Part 1: multiplying depth with horizontal position: ', x*y)

# part 2:
x = 0
y = 0
aim = 0


for i in range(0, len(direction)):
    if direction[i] == 'forward':
        x += magnitude[i]
        y += aim * magnitude[i]
    elif direction[i] == 'down':
        aim += magnitude[i]
    elif direction[i] == 'up':
        aim -= magnitude[i]

print('Part 2: multiplying depth with horizontal position: ', x*y)

