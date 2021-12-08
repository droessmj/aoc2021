import sys


class DigitConfig:
    input = ''
    output = ''
    digit_dict = {}

    def __init__(self, input, output):
        self.input = input
        self.output = output
        self.digit_dict = {}
        self.populate_digit_array()

    def populate_digit_array(self):
        input_vals = self.input.split(' ')
        print(input_vals)
        for i in input_vals:
            # do a sort to keep things consistent
            if len(i) == 2 and 1 not in self.digit_dict: # populate array for digit 1
                self.digit_dict[1] = set([c for c in i])
            elif len(i) == 3 and 7 not in self.digit_dict: # populate for 7
                self.digit_dict[7] = set([c for c in i])
            elif len(i) == 4 and 4 not in self.digit_dict:# populate for 4
                self.digit_dict[4] = set([c for c in i])
            elif len(i) == 7 and 8 not in self.digit_dict:# populate for 4
                self.digit_dict[8] = set([c for c in i])
            elif len(i) == 5 and len(self.digit_dict.keys()) == 4:
                # calc 3, 5
                # get all inputs of length 5
                length_5_vals = [val for val in input_vals if len(val) == 5]
                for val in length_5_vals:
                    if len(set(val).intersection(self.digit_dict[7])) == 3:
                        # 3
                        self.digit_dict[3] = set([c for c in val]) 
                    else:
                        self.digit_dict[5] = set([c for c in val])
            elif len(i) == 6 and len(self.digit_dict.keys()) > 4:
                # calc 2, 6, 0
                length_6_vals = [val for val in input_vals if len(val) == 6]
                for val in length_6_vals:
                    # 6
                    if len(set(val).intersection(self.digit_dict[5])) == 5:
                        self.digit_dict[6] = set([c for c in val])
                    elif len(set(val).intersection(self.digit_dict[3])) == 4: # 2
                        self.digit_dict[2] = set([c for c in val])
                    elif len(set(val).intersection(self.digit_dict[4])) == 4: # 9
                        self.digit_dict[9] = set([c for c in val])
                    else: # 0 
                        self.digit_dict[0] = set([c for c in val])

        print(sorted(self.digit_dict.keys()))

        if len(self.digit_dict.keys()) < 10:
            raise "Did not populate all values" 


    def get_output_value(self):
        count = 0
        for val in self.output.split(' '):
            set_val = set([c for c in val])
            for i in range(9):
                if self.digit_dict[i] == set_val:
                    count += i 
        return count


in_file = 'test'

if len(sys.argv) > 1:
    in_file = sys.argv[1]

count = 0
with open(f"./{in_file}.txt") as f:
    for line in f:
        parts = line.strip().split('|')
        count += DigitConfig(parts[0],parts[1]).get_output_value()

print(count)
