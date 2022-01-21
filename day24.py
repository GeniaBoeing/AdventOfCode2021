class ModelNumber:
    def __init__(self, model_number):
        self.model_number = model_number
        self.variables = [0] * 4
    def inp(self, idx, a):
        self.variables[idx] = a
    def add(self, idx_1, a):
        self.variables[idx_1] += a
    def mul(self, idx_1, a):
        self.variables[idx_1] *= a
    def div(self, idx_1, a):
        self.variables[idx_1] = int(self.variables[idx_1] / a)
    def mod(self, idx_1, a):
        self.variables[idx_1] = self.variables[idx_1] % a
    def eql(self, idx_1, a):
        if self.variables[idx_1] == a:
            self.variables[idx_1] = 1
        else:
            self.variables[idx_1] = 0 


var = {'w': 0, 'x': 1, 'y': 2, 'z': 3}

start = 99999999999999 #biggest possible model number

input_file = 'input24'
with open(input_file) as f:
    instructions = f.readlines()
instructions = [i.split() for i in instructions]


def validate_number(nr):
    pos_in_nr = 0
    for i in instructions:
        if i[0] == 'inp':
            nr.inp(var[i[1]], int(str(nr.model_number)[pos_in_nr]))
            pos_in_nr += 1
        else:
            if i[2] in 'wxyz':
                a = nr.variables[var[i[2]]]
            else:
                a = int(i[2])
 
            if i[0] == 'add':
                nr.add(var[i[1]], a) 
            elif i[0] == 'mul':
                nr.mul(var[i[1]], a)
            elif i[0] == 'div':
                nr.div(var[i[1]], a)
            elif i[0] == 'mod':
                nr.mod(var[i[1]], a)
            elif i[0] == 'eql':
                nr.eql(var[i[1]], a)
        
    if nr.variables[3] == 0:
        return True
    else:
        return False

#brute forcing it would have taken ages...
#nr = ModelNumber(start)
#
#new_number = start
#for i in range(0, start):
#    if '0' not in str(new_number): 
#        print(new_number)
#        nr = ModelNumber(new_number)
#        if validate_number(nr):
#            print('Largest model number accepted by MONAD:  ', nr.model_number)
#            break
#        else:
#            new_number = nr.model_number - 1
#    else:
#        new_number -= 1

x_adds = [12, 12, 13, 12, -3, 10, 14, -16, 12, -8, -12, -7, -6, -11]
y_adds = [7, 8, 2, 11, 6, 12, 14, 13, 15, 10, 6, 10, 8, 5]
divs = [1, 1, 1, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26, 26]

#From Gravitar64, but rewritten for my own understanding

def get_max_model_number():
    nr = [0] * 14
    stack = []
    start = 9
    
    for i in range(0, len(divs)):
        if divs[i] == 1:
            #fill a stack of an index in which inp w cycle a z div 1 instruction happens with the value that is added to y
            stack.append((i, y_adds[i]))
        else:
            #for each z div 26 instruction the stack pops and the sum of the most recently added y_add and the x_add of this
            #inp w cycle are added from which the current inp w cycle input as well as the inp w cycle input of the popped
            #cycle can be inferred
            ia, a = stack.pop()
            diff = x_adds[i] + a
            nr[ia] = min(start, start - diff)
            nr[i] = min(start, start + diff)
            print(nr) 
    return nr

def get_min_model_number():
    nr = [0] * 14
    stack = []
    start = 1
    
    for i in range(0, len(divs)):
        if divs[i] == 1:
            stack.append((i, y_adds[i]))
        else:
            ia, a = stack.pop()
            diff = x_adds[i] + a
            nr[ia] = max(start, start - diff)
            nr[i] = max(start, start + diff)
            print(nr) 
    return nr
            


print('max model number:    ', get_max_model_number())
print('min model number:    ', get_min_model_number())












