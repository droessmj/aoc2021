# method to allow for variable length initialization
def initialize(line):
    bit_counts = []
    for c in line:
        bit_counts.append(0)
    return bit_counts

count = 0
bit_counts = None
lines = []
with open("./input.txt") as f:
    for line in f:
        count += 1
        line = line.strip()
        
        if not bit_counts:
            bit_counts = initialize(line)

        bit_line = []
        for idx, c in enumerate(line):
            bit_counts[idx] += int(c)
            bit_line.append(int(c))
        lines.append(bit_line)

print(bit_counts)
gamma_list = [1 if b > count / 2.0 else 0 for b in bit_counts] 
print(gamma_list)
gamma_int = int("".join([str(i) for i in gamma_list]), 2)
epsilon_int = int("".join([str(1) if b == 0 else str(0) for b in gamma_list]), 2)
print(gamma_int * epsilon_int)

# part 1 above, part 2 below

def recalc_bit_counts(lines):
    bit_counts = None
    for line in lines:
        if not bit_counts:
            bit_counts = initialize(line)
        for idx, c in enumerate(line):
            bit_counts[idx] += int(c)
    return bit_counts

def dump_lines(lines, bit, index):
    local_lines = lines
    return_lines = []
    for l in local_lines:
        if l[index] != bit:
            return_lines.append(l)
    return return_lines

def calc_o2_rating(lines):
    local_lines = lines
    idx = 0
    while len(local_lines) > 1:
        calcd_bit_counts = recalc_bit_counts(local_lines)
        b = calcd_bit_counts[idx]
        count = len(local_lines)
        if b >= count / 2.0:
            # if this, we want to keep 1
            local_lines = dump_lines(local_lines, 0, idx)            
        else:
            local_lines = dump_lines(local_lines, 1, idx)            
        idx+=1

    #assumes we have one list of bit values at this point
    return int("".join([str(0) if b == 0 else str(1) for b in local_lines[0]]), 2)

def calc_co2_rating(lines):
    local_lines = lines
    idx = 0
    while len(local_lines) > 1:
        calcd_bit_counts = recalc_bit_counts(local_lines)
        b = calcd_bit_counts[idx]
        count = len(local_lines)
        if b < count / 2.0:
            # if this, we want to keep 1
            local_lines = dump_lines(local_lines, 0, idx)            
        else:
            local_lines = dump_lines(local_lines, 1, idx)            
        idx+=1

    #assumes we have one list of bit values at this point
    return int("".join([str(0) if b == 0 else str(1) for b in local_lines[0]]), 2)

o2_rating = calc_o2_rating(lines)
print(o2_rating)
co2_rating = calc_co2_rating(lines)
print(co2_rating)
print(co2_rating * o2_rating)
