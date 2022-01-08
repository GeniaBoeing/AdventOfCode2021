import re
import numpy as np

input_file = 'input22'

with open(input_file) as f:
    lines = f.readlines()

lines = [list(re.findall(r'(on|off) x=([-0-9]+)\.\.([-0-9]+),y=([-0-9]+)\.\.([-0-9]+),z=([-0-9]+)\.\.([-0-9]+)', i)[0]) for i in lines]

for i in range(0, len(lines)):
    for j in range(1, len(lines[i])):
        lines[i][j] = int(lines[i][j])

reboot_steps = lines
print(reboot_steps)

dimension = 50

grid = np.zeros((dimension*2 + 1, dimension*2 + 1, dimension*2 + 1))

def adjust_reboot_step_within_bounds(reboot_step):
    for i in range(1, len(reboot_step), 2):
        if reboot_step[i] < -dimension and reboot_step[i+1] < -dimension:
            return []
        if reboot_step[i] > dimension and reboot_step[i+1] > dimension:
            return []
        if not(-dimension <= reboot_step[i]):
            reboot_step[i] = -dimension
        if not(reboot_step[i] <= dimension):
            reboot_step[i] = dimension
    return reboot_step
        


def rebooting(grid, reboot_steps):
    for i in range(0, len(reboot_steps)):
        reboot_steps[i] = adjust_reboot_step_within_bounds(reboot_steps[i])
        if reboot_steps[i]:
            for x in range(reboot_steps[i][1], reboot_steps[i][2]+1):
                for y in range(reboot_steps[i][3], reboot_steps[i][4]+1):
                    for z in range(reboot_steps[i][5], reboot_steps[i][6]+1):
                        x_idx = x + dimension
                        y_idx = y + dimension
                        z_idx = z + dimension
                        if reboot_steps[i][0] == 'on':
                            grid[x_idx][y_idx][z_idx] = 1
                        else:
                            grid[x_idx][y_idx][z_idx] = 0
    return grid

def get_nr_on_cubes(grid):
    nr_on = 0
    for x in range(0, 2*dimension + 1):
        for y in range(0, 2*dimension + 1):
            for z in range(0, 2*dimension + 1):
                if grid[x][y][z] == 1:
                    nr_on += 1
    return nr_on

grid = rebooting(grid, reboot_steps)
print('nr of cubes on after reboot  ', get_nr_on_cubes(grid))
