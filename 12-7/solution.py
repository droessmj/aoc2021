import sys

lookup_deltas = {}

# (3, 6)
def calc_deltas(n):
    if n not in lookup_deltas:
        delta_val = sum(range(1,n+1))
        lookup_deltas[n] = delta_val
    return lookup_deltas[n]

def calc_distance_seed(seed, inputs, running_best):
    total = 0
    for i in inputs:
        delta = calc_deltas(abs(seed-i))
        total += delta

        # bail early
        if total > running_best:
            return running_best

    return total


def calc_distance(inputs):
    running_best = sys.maxsize
    list_min = min(input_list)
    list_max = max(input_list)

    for i in range(list_min, list_max):
        dist = calc_distance_seed(i, inputs, running_best)
        if dist < running_best:
            running_best = dist

    return running_best

in_file = 'test'

if len(sys.argv) > 1:
    in_file = sys.argv[1]

with open(f'./{in_file}.txt') as f:
    input = f.readline().strip()
    input_list = [int(n) for n in input.split(',')]
    print(calc_distance(input_list))
