import sys

def calc_fish(start_val, target_days):
    day_idx = 0
    fish_list = [start_val]
    while day_idx < target_days:
        new_fish_count = 0

        for idx, _ in enumerate(fish_list):
            if fish_list[idx] == 0:
                fish_list[idx] = 6
                new_fish_count += 1
            else:
                fish_list[idx] -= 1

        if new_fish_count > 0:
            fish_list.extend([8 for f in range(new_fish_count)])

        day_idx += 1 

    return len(fish_list)



lookup_table = {}

target_days = int
if len(sys.argv) > 1:
    target_days = int(sys.argv[1])
else:
    target_days = 80

with open("./input.txt") as f:
    input = f.read()
    starting_fish = [int(n) for n in input.split(',')]
    final_count = 0
    for start_value in starting_fish:
        if start_value in lookup_table:
            final_count += lookup_table[start_value]
        else:
            descendant_count = calc_fish(start_value, target_days)
            print(f"Calculated value for {start_value}: {descendant_count}")
            lookup_table[start_value] = descendant_count
            final_count += descendant_count
    
    print(final_count)