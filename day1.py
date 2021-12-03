def nr_increases(a):
    nr_increases = 0
    for i in range(0, len(a)-1):
        if a[i+1] > a[i]:
            nr_increases += 1
    return nr_increases




input_file = '/Users/genia/Desktop/AdventOfCode2021/input'
input = []
with open(input_file) as f:
    for line in f:
        input.append(int(line))

#input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

increases_depth_measurement = nr_increases(input)

print('Number of times the depth measurement increased: ', increases_depth_measurement)

#three measurement sliding window sums

three_sum = [0]*(len(input)-2)
for i in range(0, len(input)-2):
    three_sum[i] = input[i] + input[i+1] + input[i+2]

increases_three_sum = nr_increases(three_sum)
print('Number of times the three measurement sliding window sum increased: ', increases_three_sum)
