input_file = 'input14'

with open(input_file) as f:
    lines = f.readlines()
template = lines[0].strip() 

rules = [lines[i].strip() for i in range(2, len(lines))]
rules = [l.split(' -> ') for l in rules]
rules_dict = {}
pairs = {}
for i in rules:
    rules_dict[i[0]] = i[1]
    pairs[i[0]] = 0
rules = rules_dict



for i in range(0, len(template) - 1):
    pairs[template[i]+template[i+1]] += 1
ele = {}
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    ele[i] = 0
for t in template:
    ele[t] += 1

def step(pairs, ele):
    loc_pairs = pairs.copy()
    for p in pairs.keys():
        ele[rules[p]] += pairs[p]
        loc_pairs[p[0] + rules[p]] += pairs[p] 
        loc_pairs[rules[p] + p[1]] += pairs[p]
        loc_pairs[p] -= pairs[p]
    return loc_pairs, ele

steps = 40
for i in range(0, steps):
    pairs, ele = step(pairs, ele)
counts = ele.values()
counts = [i for i in counts if i != 0]
print('difference   ', max(counts) - min(counts))




