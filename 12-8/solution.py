import sys

in_file = 'test'

if len(sys.argv) > 1:
    in_file = sys.argv[1]

count = 0
with open(f"./{in_file}.txt") as f:
    for line in f:
        parts = line.strip().split('|')
        output = parts[1]
        for result in output.split(' '):
            length = len(result)
            if length == 2 or length == 3 or length == 4 or length == 7:
                count += 1

print(count)