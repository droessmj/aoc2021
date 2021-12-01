increased_count = 0
all_readings = []

with open("./input.txt") as f:
    prior_reading = None
    for line in f:
        current_reading = int(line)
        all_readings.append(current_reading)
        if prior_reading and current_reading > prior_reading:
            increased_count +=1 
        prior_reading = current_reading

print(increased_count)
### ^^ Part A solution (added list of all_readings for Part B)

### Part B below

increased_count = 0
# start at index 0, progress while less than len(list) - 2?
# take 0,1,2 and calc value --> prior reading
# current reading > prior reading? -- increased_count = 0
index = 0
prior_reading = None
while index < len(all_readings)-2:
    current_reading = all_readings[index] + all_readings[index+1] + all_readings[index+2]
    if prior_reading and current_reading > prior_reading:
        increased_count += 1
    prior_reading = current_reading
    index+=1
print(increased_count)