# method to allow for variable length initialization
def initialize(line):
    bit_counts = []
    for c in line:
        bit_counts.append(0)
    return bit_counts

count = 0
bit_counts = None

with open("./input.txt") as f:
    for line in f:
        count += 1
        line = line.strip()
        if not bit_counts:
            bit_counts = initialize(line)

        for idx, c in enumerate(line):
            bit_counts[idx] += int(c)

print(bit_counts)
gamma_list = [1 if b > count / 2.0 else 0 for b in bit_counts] 
print(gamma_list)
gamma_int = int("".join([str(i) for i in gamma_list]), 2)
epsilon_int = int("".join([str(1) if b == 0 else str(0) for b in gamma_list]), 2)
print(gamma_int * epsilon_int)

# part 1 above
