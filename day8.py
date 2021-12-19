input_file = 'input8'

with open(input_file) as f:
    lines = f.readlines()

output = [0] * len(lines)
input = [0] * len(lines)
for i in range(0, len(lines)):
    output[i] = (lines[i].strip()).split(' | ')[1]
    output[i] = output[i].split(' ')
    
    input[i] = (lines[i].strip()).split(' | ')[0]
    input[i] = input[i].split(' ')


#part 1
digit_nr = [0]* 10
for i in range(0, len(output)):
    for n in output[i]:
        if len(n) == 2:
            digit_nr[1] += 1
        if len(n) == 4:
            digit_nr[4] += 1
        if len(n) == 3:
            digit_nr[7] += 1
        if len(n) == 7:
            digit_nr[8] += 1

counter = sum(digit_nr)
print('nr of 1, 4, 7, 8: ', counter)

#part 2

def digit_correspondence(input):
    correspondence = {}
    for i in 'abcdefg':
        correspondence[i] = ''
    
    for i in input:
        if len(i) == 2:
            correspondence['c'] = i
            correspondence['f'] = i
    
    for i in input:
        if len(i) == 3:
            for char in i:
                if char not in correspondence['c']:
                    correspondence['a'] = char

    for i in input:
        if len(i) == 4:
            for char in i:
                if char not in correspondence['c']:
                    correspondence['b'] = correspondence['b'] + char
                    correspondence['d'] = correspondence['d'] + char

    for i in input:
        if len(i) == 5:
            tmp = i.replace(correspondence['a'], '')
            tmp = tmp.replace(correspondence['b'][0], '')
            tmp = tmp.replace(correspondence['b'][1], '')
            tmp = tmp.replace(correspondence['c'][0], '')
            tmp = tmp.replace(correspondence['c'][1], '')
            if len(tmp) == 1:
                correspondence['g'] = tmp

    for i in input:
        if len(i) == 5:
            tmp = i.replace(correspondence['a'], '')
            tmp = tmp.replace(correspondence['b'][0], '')
            tmp = tmp.replace(correspondence['b'][1], '')
            tmp = tmp.replace(correspondence['c'][0], '')
            tmp = tmp.replace(correspondence['c'][1], '')
            tmp = tmp.replace(correspondence['g'], '')
            if len(tmp) == 1:
                correspondence['e'] = tmp
                for char in i:
                    if char in correspondence['c']:
                        c = char
    correspondence['c'] = c
    correspondence['f'] = correspondence['f'].replace(c, '')

    for i in input:
        if len(i) == 5:
            tmp = i.replace(correspondence['a'], '')
            tmp = tmp.replace(correspondence['c'], '') 
            tmp = tmp.replace(correspondence['f'], '')
            tmp = tmp.replace(correspondence['g'], '')
            tmp = tmp.replace(correspondence['e'], '') 
            
            if len(tmp) == 1:
                correspondence['d'] = tmp
                correspondence['b'] = correspondence['b'].replace(tmp, '')  


    return correspondence
normal_digits = [0] * 10
normal_digits[0] = 'abcefg'
normal_digits[1] = 'cf'
normal_digits[2] = 'acdeg'
normal_digits[3] = 'acdfg'
normal_digits[4] = 'bcdf'
normal_digits[5] = 'abdfg'
normal_digits[6] = 'abdefg'
normal_digits[7] = 'acf'
normal_digits[8] = 'abcdefg'
normal_digits[9] = 'abcdfg'

counter = 0
for i in range(0, len(lines)):
    correspondence = digit_correspondence(input[i])
    inv_map = {v: k for k, v in correspondence.items()}
    str_nr = ''
    for o in output[i]:
        str_rep = ''
        for char in o:
            str_rep += inv_map[char]
        for nr in range(0, len(normal_digits)):
            if sorted(str_rep) == sorted(normal_digits[nr]):
                str_nr  += str(nr)
    counter += int(str_nr)
    
print(counter)





    

