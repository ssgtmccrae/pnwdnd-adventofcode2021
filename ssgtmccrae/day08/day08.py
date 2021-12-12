"""
Ryan McGregor, 11Dec2021
AOC2021:Day08
https://adventofcode.com/2021/day/8
Been really busy, tornadoes and stuff...
"""
from typing import List, OrderedDict
from aocd import get_data
import sys
from pprint import pprint

test_set =  [{'debug_code': ['agedc', 'cf', 'cdeagf', 'agcf', 'cbefda', 'fdcge', 'cdgaeb', 'bedgf', 'dcf', 'gbcaefd'],
              'output': ['gdefb', 'fc', 'egcad', 'abecgd']}]

# seven_digit = {
#     'top': None,
#     'upper_left': None,
#     'upper_right': None,
#     'middle': None,
#     'lower_left': None,
#     'lower_right': None,
#     'bottom': None
# }

def decrypt_displays(seven_dig_outputs: List[OrderedDict]):
    """
    Attempts to decrypt a list of display outputs based on debug_code and output.
    Input: List of OrderedDicts containing debug_code and output portions of output, split into lists.
    Output: List of OrderedDicts, containing original input, seven_digit wiring map, and best guessed output.
    """
    output = []
    for number_set in seven_dig_outputs:
        output_data = {'input': number_set, 'legend': {}, 'decoded_output': []}
        for number in number_set['debug_code']:
            sorted_number = ''.join(sorted(number))
            if len(sorted_number) == 2:
                output_data['legend'][sorted_number] = '1'
            if len(sorted_number) == 4:
                output_data['legend'][sorted_number] = '4'
            if len(sorted_number) == 3:
                output_data['legend'][sorted_number] = '7'
            if len(sorted_number) == 7:
                output_data['legend'][sorted_number] = '8'
        for number in number_set['output']:
            sorted_number = ''.join(sorted(number))
            try:
                output_data['decoded_output'].append(output_data['legend'][sorted_number])
            except:
                output_data['decoded_output'].append(None)
        output.append(output_data)
    return output

if __name__ == '__main__':
    dataset = []
    for line in get_data(year=2021, day=8).split('\n'):
        frame = {}
        # Pesky whitespace generates empty list items.
        frame['debug_code'] = [x for x in line.split('|')[0].split(' ') if x != '']
        frame['output'] =  [x for x in line.split('|')[1].split(' ') if x != '']
        dataset.append(frame)

# pprint(decrypt_displays(test_set))

decrypted_displays = decrypt_displays(dataset)

pprint(decrypted_displays)

total = 0
for display in decrypted_displays:
    for number in display['decoded_output']:
        if number in ['1','4','7','8']:
            total += 1
print(total)
