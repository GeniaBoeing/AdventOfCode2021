import math
import numpy as np

input_file = 'input7'
#input_file = 'ex7.txt'

with open(input_file) as f:
    line = f.readlines()

input = (line[0].strip()).split(',')
input = [int(i) for i in input]

def cost_horizontal_position(input, pos):
    cost = 0
    for i in input:
        cost += abs(i - pos)
    return cost


pos = np.median(input) 
cost = cost_horizontal_position(input, pos)
print('pos  ' , pos, ' cost    ', cost)

#part2
def crab_fuel_cost(input, pos):
    cost = 0
    for i in input:
        cost += (pos - i)**2 + abs(pos - i)
    cost = 0.5 * cost
    return cost

min_pos = np.min(input)
max_pos = np.max(input)
print(max_pos)

pos = min_pos
cost = crab_fuel_cost(input, pos)
for i in range(min_pos, max_pos + 1):
    tmp_cost = crab_fuel_cost(input, i)
    if tmp_cost < cost:
        pos = i
        cost = tmp_cost

print('pos  ' , pos, ' cost    ', cost)

