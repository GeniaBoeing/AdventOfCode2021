input = 'target area: x=20..30, y=-10..-5'
xmin = 288
xmax = 330
ymin = -96
ymax = -50

def step(x, y, v_x, v_y):
    x += v_x
    y += v_y
    if v_x < 0:
        v_x += 1
    elif v_x > 0:
        v_x -= 1
    v_y -= 1
    return x, y, v_x, v_y


def is_in_target(x,y):
    if xmin <= x <= xmax and ymin <= y <= ymax:
        return True
    return False    

def is_past_target(x,y):
    if x > xmax or y < ymin:
        return True
    return False

v_x_max = xmax
v_y_max = abs(ymin)
max_height = 0
max_v_x = 0
max_v_y = 0
for i in range(0, v_x_max):
    for j in range(-v_y_max, v_y_max):
        x = 0
        y = 0 
        tmp_height = 0       
        while(not (is_in_target(x, y) or is_past_target(x, y))):
            x, y, i, j = step(x, y, i, j)
            if y > tmp_height: tmp_height = y
        if is_in_target: 
            if tmp_height > max_height: max_height = tmp_height

print('max height   ', max_height)
