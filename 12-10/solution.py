import sys



in_file = 'test'

if len(sys.argv) > 1:
    in_file = sys.argv[1]

count = 0

openers = {'{','[','(','<'}
closers = {'}',']',')','>'}
pairs = {
    '}':'{',
    '{':'}',
    ']':'[',
    '[':']',
    '>':'<',
    '<':'>',
    ')':'(',
    '(':')'
}
score = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

autocomplete_score = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

count = 0
good_lines = []
good_line_stack = []
with open(f"./{in_file}.txt") as f:
    for line in f:
        stack = []
        line = line.strip()
        line_good = True
        for c in line:
            if c in openers:
                stack.append(c)
            else: # c in closers
                try:
                    p = stack.pop()
                    if p != pairs[c]:
                        line_good = False
                        break
                except: # empty list with a closer
                    line_good = False
                    break
        if line_good:
            good_lines.append(line)
            good_line_stack.append(stack)


all_scores = []
for idx,line in enumerate(good_lines):
    stack = good_line_stack[idx]
    stack.reverse()
    answer = []
    score = 0
    for c in stack:
        answer.append(pairs[c])
        score = score * 5 + autocomplete_score[pairs[c]]
    all_scores.append(score)

all_scores.sort()
print(all_scores[int(len(all_scores) / 2)])