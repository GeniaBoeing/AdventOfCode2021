input ='[[[[[9,8],1],2],3],4]'
#input = '[7,[6,[5,[4,[3,2]]]]]'
#input = '[[6,[5,[4,[3,2]]]],1]'
#input = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
#input = '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
#input = '[[[[3,0],[5,3]],[4,4]],[5,5]]'
#input = '[[[[1,1],[2,2]],[3,3]],[4,4]]'
def split(num): #leftmost number is split
    depth = 0
    for i in range(0, len(num)): 
        if num[i] == '[':
            depth += 1
        elif num[i] == ']':
            depth -= 1

        if num[i-1] in '123456789' and num[i] in '1234567890' and depth < 5:
            to_split = int(num[i-1:i+1])
            new_string = '[' + str(int(to_split/2)) + ',' + str(int(to_split/2) + (to_split % 2 > 0)) + ']'
            num = num[:i-1] + new_string + num[i+1:]
            return num
    return num

def explode(num): #leftmost pair explodes first
    depth = 0
    for i in range(0, len(num)):
        if num[i] == '[':
            depth += 1
        elif num[i] == ']':
            depth -= 1
         
        if (depth == 5 and 
            num[i+1] in '1234567890' and
            (num[i+2] != '[' and num[i+3] !=  '[')
            and num[i] != ','
            ): # just check at right depth and reached numbers
            if num[i+2] in '1234567890':#left number larger than 9
                left = num[i+1:i+3]
                if num[i+5] in '1234567890':
                    right = num[i+4:i+6]
                    end_bracket = i+6
                else:
                    right = num[i+4]
                    end_bracket = i+5
            else:
                left = num[i+1]
                if num[i+4] in '1234567890':
                    right = num[i+3:i+5]
                    end_bracket = i+5
                else:
                    right = num[i+3]
                    end_bracket = i+4
            
            for l in range(i, -1, -1):
                if num[l] in '1234567890':
                    if num[l-1] not in '1234567890':
                        left = str(int(num[l]) + int(left))
                        length_left = 0
                    else:
                        left = str(int(num[l-1:l+1]) + int(left))
                        length_left = 1
                    break
            #this also needs to be adapted for >9 numbers
            for r in range(end_bracket, len(num)):
                if num[r] in '1234567890':
                    if num[r+1] not in '1234567890':
                        right = str(int(num[r]) + int(right))
                        length_right = 1
                    else:
                        right = str(int(num[r:r+2]) + int(right))
                        length_right = 2
                    break
            #right bounds need to be adapted to >9 numbers
            if l == 0:
                num = num[:4] + '0' + num[end_bracket+1:r] + right + num[r+length_right:]
            elif r == len(num) - 1:
                num = num[:l-length_left] + left +',0' + num[end_bracket+1:]
            else:
                num = num[:l-length_left] + left + num[l+1:i] + '0' + num[end_bracket+1:r] + right + num[r+length_right:]
            return num
    return num

def reduce(num):
    changed = True
    length_num = len(num)
    while(changed):
        tmp = num
        do_action = True
        while(do_action):
            len_ex = len(num)
            num = explode(num)
            if len_ex == len(num):
                do_action = False
        num = split(num) 
        length_num = len(num)
        if tmp == num:
            changed = False
    return num

import re
from ast import literal_eval 
def magnitude(num): 
    nested_list = literal_eval(re.sub('([A-Za-z])', r'"\1"', str(num)))
    
    if isinstance(nested_list[0], list):
        nested_list[0] = magnitude(nested_list[0])
    
    if isinstance(nested_list[1], list):
        nested_list[1] = magnitude(nested_list[1])
                  

    if isinstance(nested_list[0], int)  and isinstance(nested_list[1], int):
        return nested_list[0] * 3 + nested_list[1] * 2
input_file = 'input18'
with open(input_file) as f:
    lines = f.readlines()
for i in range(0, len(lines)):
    lines[i] = lines[i].strip()

sum_num = lines[0]
for i in range(1, len(lines)):
    sum_num ='[' + sum_num + ',' + lines[i] + ']'
    sum_num = reduce(sum_num)
print('final', sum_num)

print('magnitude:   ', magnitude(sum_num))

magnitudes = []
for i in range(0, len(lines)):
    for j in range(0, len(lines)):    
        sum_num ='[' + lines[i] + ',' + lines[j] + ']'
        sum_num = reduce(sum_num)
        magnitudes.append(magnitude(sum_num))
        sum_num ='[' + lines[j] + ',' + lines[i] + ']'
        sum_num = reduce(sum_num)
        magnitudes.append(magnitude(sum_num))

print('max magnitude:   ', max(magnitudes))
