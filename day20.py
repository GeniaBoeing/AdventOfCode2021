input_file  = 'input20'

with open(input_file) as f:
    lines = f.readlines()

image_algorithm = lines[0]
image_input = [lines[i].strip() for i in range(2, len(lines))]
print(len(image_input))
def get_next_value(image, x, y):
    bin_str = ''
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if image[i][j] == '.':
                bin_str += '0'
            else:
                bin_str += '1'
    nr = int(bin_str, 2)
    value = image_algorithm[nr]  
    return value

def get_new_infinity_pixel(infinity_pixel):
    if infinity_pixel == '.':
        bin_str = '0'*9
    else:
        bin_str = '1'*9 
    value = image_algorithm[int(bin_str, 2)]
    return value


def step(image, infinity_pixel):
    new_image = [[0 for i in range(len(image[0]) + 4)] for j in range(len(image) + 4)]
    for i in range(0, len(image)+4):
        for j in range(0, len(image[0]) + 4):
            if j <= 1 or j >= len(image[0]) + 2:
                new_image[i][j] = infinity_pixel
            if i <= 1 or i >= len(image) + 2:
                new_image[i][j] = infinity_pixel
            if 1 < i < len(image) + 2 and 1 < j < len(image[0]) + 2:
                new_image[i][j] = image[i-2][j-2]

    new_infinity_pixel = get_new_infinity_pixel(infinity_pixel)

    next_image = [[0 for i in range(len(image[0]) + 4)] for j in range(len(image) + 4)]
    for i in range(1, len(image)+3):
        for j in range(1, len(image)+3):
            next_image[i][j] = get_next_value(new_image, j, i)
    for i in range(0, len(next_image)):
        for j in range(0, len(next_image[0])):
            if i == 0 or i == len(next_image)-1:
                next_image[i][j] = new_infinity_pixel
            if j == 0 or j == len(next_image[0])-1:
                next_image[i][j] = new_infinity_pixel

    return next_image, new_infinity_pixel

steps = 50
image = image_input
infinity_pixel = '.'

for i in range(0, steps):
    image, infinity_pixel = step(image, infinity_pixel)

nr_lit = 0
for i in range(0, len(image)):
    for j in range(0, len(image[0])):
        if image[i][j] == '#':
            nr_lit += 1

print('number of lit pixels after ', steps, ' steps is: ', nr_lit)



