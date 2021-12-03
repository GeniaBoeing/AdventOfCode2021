input_file = '/Users/genia/Desktop/AdventOfCode2021/input'
input = []
with open(input_file) as f:
    for line in f:
        input.append(int(line))

increases_depth_measurement = 0

for i in range(0, len(input)-1):
    if input[i+1] > input[i]:
        increases_depth_measurement += 1

print('Number of times the depth measurement increased: ', increases_depth_measurement)
