import sys

def calc_fish(start_val, target_days):
    if (start_val,target_days) in lookup_table:
        return lookup_table[(start_val,target_days)]
    elif target_days == 0:
        return 1
    else: 
        # add to lookup table or recursively call?
        result = 0
        if start_val == 0:
            result = calc_fish(6, target_days-1)
            result += calc_fish(8, target_days-1)
        else:
            result = calc_fish(start_val-1, target_days-1)        
            
        lookup_table[(start_val,target_days)] = result
        return result



lookup_table = {}
init_table = {}

target_days = int
if len(sys.argv) > 1:
    target_days = int(sys.argv[1])
else:
    target_days = 1

with open("./input.txt") as f:
    input = f.read()
    starting_fish = [int(n) for n in input.split(',')]
    final_count = 0
    for start_value in starting_fish:
        if start_value in init_table:
            final_count += init_table[start_value]
        else:
            descendant_count = calc_fish(start_value, target_days)
            init_table[start_value] = descendant_count
            final_count += descendant_count
    
    print(final_count)