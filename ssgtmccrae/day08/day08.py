"""
Ryan McGregor, 11Dec2021
AOC2021:Day08
https://adventofcode.com/2021/day/8
Been really busy, tornadoes and stuff...
"""
from typing import List, OrderedDict
from aocd import get_data

test_set =  [{'debug_code': ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'],
               'output': ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']}]

seven_digit = {
    'top': None,
    'upper_left': None,
    'upper_right': None,
    'middle': None,
    'lower_left': None,
    'lower_right': None,
    'bottom': None
}

def decrypt_displays(seven_dig_outputs: List[OrderedDict]):
    """
    Attempts to decrypt a list of display outputs based on debug_code and output.
    Input: List of OrderedDicts containing debug_code and output portions of output, split into lists.
    Output: List of OrderedDicts, containing original input, seven_digit wiring map, and best guessed output.
    """
    output = []
    for number_set in seven_dig_outputs:
        output_data = {'input': number_set, 'inverse_legend': {}, 'legend': {}, 'seven_digit': seven_digit, 'decoded_output': []}
        # Find positions in legend.Eight
        for number in [x for x in number_set['debug_code'] if len(x) == 7]:
            output_data['legend']['8'] = ''.join(sorted(number))
        # Find positions in legend.One
        for number in [x for x in number_set['debug_code'] if len(x) == 2]:
            output_data['legend']['1'] = ''.join(sorted(number))
        # Find positions in legend.Seven
        for number in [x for x in number_set['debug_code'] if len(x) == 3]:
            output_data['legend']['7'] = ''.join(sorted(number))
        # Find seven_digit.Top using legend.Seven
        output_data['seven_digit']['top'] = [x for x in list(output_data['legend']['7']) if x not in list(output_data['legend']['1'])]
        # Find positions in legend.Four
        for number in [x for x in number_set['debug_code'] if len(x) == 4]:
            output_data['legend']['4'] = ''.join(sorted(number))
        # Find positions in legends.Zero
        zero_potentials = [x for x in number_set['debug_code'] if len(x) == 6]
        for number in zero_potentials:
            if (len([x for x in list(output_data['legend']['4']) if x not in list(number)]) == 1
                and len([x for x in list(output_data['legend']['1']) if x not in list(number)]) == 0):
                output_data['legend']['0'] = ''.join(sorted(number))
        # Find seven_digit.Middle
        output_data['seven_digit']['middle'] = [x for x in list(output_data['legend']['8']) if x not in list(output_data['legend']['0'])]
        # Find seven_digit.Upper_Left
        output_data['seven_digit']['upper_left'] = [x for x in output_data['legend']['4'] if x not in output_data['legend']['1']
                                                    and x not in output_data['seven_digit']['middle']]
        # Find positions in legends.Two
        two_potentials = [x for x in number_set['debug_code'] if len(x) == 5]
        for number in two_potentials:
            if (output_data['seven_digit']['upper_left'][0] not in list(number)
                and len([x for x in list(output_data['legend']['1']) if x not in list(number)]) == 1):
                output_data['legend']['2'] = ''.join(sorted(number))
        # Find seven_digit.Lower_Right
        output_data['seven_digit']['lower_right'] = [x for x in output_data['legend']['1'] if x not in output_data['legend']['2']]
        # Find seven_digit.Upper_Right
        output_data['seven_digit']['upper_right'] = [x for x in output_data['legend']['1'] if x not in list(output_data['seven_digit']['lower_right'])]
        # Find positions in legends.Nine
        nine_potentials = [x for x in number_set['debug_code'] if len(x) == 6]
        for number in nine_potentials:
            if len([x for x in list(number) if x not in output_data['legend']['7'] + output_data['legend']['4']]) == 1:
                output_data['legend']['9'] = ''.join(sorted(number))
        # Find seven_digit.Bottom
        output_data['seven_digit']['bottom'] = [x for x in output_data['legend']['9'] if x not in output_data['legend']['7'] + output_data['legend']['4']]
        # Find seven_digit.Lower_Left
        output_data['seven_digit']['lower_left'] = [x for x in output_data['legend']['8'] if x not in output_data['legend']['9']]
        # Find positions in legends.Three
        output_data['legend']['3'] = ''.join([x for x in output_data['legend']['9'] if x not in output_data['seven_digit']['upper_left']])
        # Find positions in legends.Five
        output_data['legend']['5'] = ''.join([x for x in output_data['legend']['9'] if x not in output_data['seven_digit']['upper_right']])
        # Find positions in legends.Six
        output_data['legend']['6'] = ''.join(sorted(list(output_data['legend']['5']) + (output_data['seven_digit']['lower_left'])))


        # Generate Inverse Legend
        output_data['inverse_legend'] = {value:key for key, value in output_data['legend'].items()}
        # Decode output
        for number in number_set['output']:
            sorted_number = ''.join(sorted(number))
            output_data['decoded_output'].append(output_data['inverse_legend'][sorted_number])
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

    # decrypted_displays = decrypt_displays(test_set) # Test code
    decrypted_displays = decrypt_displays(dataset)
    # pprint(decrypted_displays) # Test code

    # Pt1
    pt1_total = 0
    for display in decrypted_displays:
        for item in display['decoded_output']:
            if item in ['1','4','7','8']:
                pt1_total += 1
    print(f'==Part One Answer== \n{pt1_total}')

    # Pt2
    pt2_total = 0
    for display in decrypted_displays:
        pt2_total += int(''.join(display['decoded_output']))
    print(f'==Part Two Answer== \n{pt2_total}')
