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
counter = 0
for start_i in range(0, v_x_max + 1):
    for start_j in range(-v_y_max, v_y_max + 1):
        x = 0
        y = 0 
        tmp_height = 0       
        i = start_i 
        j = start_j
        while(not (is_in_target(x, y) or is_past_target(x, y))):
            x, y, i, j = step(x, y, i, j)
            if y > tmp_height: tmp_height = y
        if is_in_target(x, y): 
            counter += 1
            if tmp_height > max_height: max_height = tmp_height
print('max height   ', max_height)
print('nr distinct starting v   :', counter)

