loc = [0,0]
with open("./input.txt") as f:
    for line in f:
        reading = line.split(' ')
        if reading[0] == "forward":
            loc[0] += int(reading[1])
        elif reading [0] == "down":
            loc[1] += int(reading[1])
        else:
            loc[1] -= int(reading[1])

print(loc)
print(loc[0]*loc[1])


## part 1 above, part 2 below

# horizontal, depth, aim
loc = [0,0,0]
with open("./input.txt") as f:
    for line in f:
        reading = line.split(' ')
        if reading[0] == "forward":
            loc[0] += int(reading[1])
            loc[1] += int(reading[1]) * loc[2]
        elif reading [0] == "down":
            loc[2] += int(reading[1])
        else:
            loc[2] -= int(reading[1])
        print(loc)

print(loc)
print(loc[0]*loc[1])

