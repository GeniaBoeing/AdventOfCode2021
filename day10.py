input_file = 'input10'

with open(input_file) as f:
    lines = f.readlines()
lines = [l.strip() for l in lines]
print('check if last line empty ', lines[-1])

illegal_score = {')': 3, ']': 57, '}': 1197, '>':  25137}
brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
autocomplete_score = {'(': 1, '[': 2, '{': 3, '<': 4}
syntax_error_score = 0
autocomplete_scores = []

for line in lines:
    open_chunk = ''
    illegal = False
    for b in line:
        if b in ')]}>':
            if open_chunk[-1] == brackets[b]:
                open_chunk = open_chunk[:-1]
            else:
                syntax_error_score += illegal_score[b]
                illegal = True
                break
        else:
            open_chunk += b
    if not illegal:
        score = 0
        for i in range(len(open_chunk) - 1, -1, -1):
            score =  5*score + autocomplete_score[open_chunk[i]]
        autocomplete_scores.append(score)
    


print('syntax error score   ', syntax_error_score)
autocomplete_scores.sort()
print('middle autocomplete score:   ', autocomplete_scores[len(autocomplete_scores)//2])  
