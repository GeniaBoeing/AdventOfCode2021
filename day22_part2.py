import re
import numpy as np

# idea and implementation basically from ai_prof on reddit


input_file = 'input22'

with open(input_file) as f:
    lines = f.readlines()

lines = [list(re.findall(r'(on|off) x=([-0-9]+)\.\.([-0-9]+),y=([-0-9]+)\.\.([-0-9]+),z=([-0-9]+)\.\.([-0-9]+)', i)[0]) for i in lines]

for i in range(0, len(lines)):
    for j in range(1, len(lines[i])):
        lines[i][j] = int(lines[i][j])

reboot_steps = lines

def intersection(cuboid_1, cuboid_2):
    intersection_cuboid = [0]*7
    intersection_cuboid[1] = max(cuboid_1[1], cuboid_2[1])
    intersection_cuboid[2] = min(cuboid_1[2], cuboid_2[2])        
    if intersection_cuboid[1] > intersection_cuboid[2]: return None    

    intersection_cuboid[3] = max(cuboid_1[3], cuboid_2[3])
    intersection_cuboid[4] = min(cuboid_1[4], cuboid_2[4])        
    if intersection_cuboid[3] > intersection_cuboid[4]: return None

    intersection_cuboid[5] = max(cuboid_1[5], cuboid_2[5])
    intersection_cuboid[6] = min(cuboid_1[6], cuboid_2[6])        
    if intersection_cuboid[5] > intersection_cuboid[6]: return None
    
    if cuboid_2[0] == 'off':
        intersection_cuboid[0] = 'on'
    else:
        intersection_cuboid[0] = 'off'

    return intersection_cuboid

cuboids = []
for r in range(0, len(reboot_steps)):
    toadd = [reboot_steps[r]] if reboot_steps[r][0] == 'on' else []
    for cuboid in cuboids:
        inter = intersection(reboot_steps[r], cuboid)
        if inter:
            toadd += [inter]
    cuboids += toadd

def nr_on_cubes(cuboids):
    nr_on = 0
    for c in cuboids:
        sign = 0
        if c[0] == 'on': sign = 1
        else: sign = -1 
        nr_on += sign * (c[2] - c[1] + 1) * (c[4] - c[3] + 1) * (c[6] - c[5] + 1)
    return nr_on

print('nr cubses on: ', nr_on_cubes(cuboids)) 


