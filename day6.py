def get_next_state(state):    
    nr_baby_fishies = 0
    for fish in range(0, len(state)):
        if state[fish] > 0:
            state[fish] -= 1
        elif state[fish] == 0:
            state[fish] = 6
            nr_baby_fishies += 1

    babies = [8]*nr_baby_fishies
    state = state + babies
    return state


input_file = 'input6'

with open(input_file) as f:
    lines = f.readlines()


end_day = 256
initial_state = (lines[0].strip()).split(',')
print(initial_state)

state = [int(i) for i in initial_state]
fishies = [0]*9
for i in state:
    fishies[i] += 1

for i in range(0, end_day):
    ready_fishies = fishies[0]
    fishies[0] = 0
    for k in range(1, 9):
        fishies[k-1] = fishies[k]

    fishies[8] = ready_fishies
    fishies[6] += ready_fishies

    print(fishies)

nr_fishies = 0
for i in fishies:
    nr_fishies += i

print('nr of fish after ', end_day, ' days : ', nr_fishies)



        

