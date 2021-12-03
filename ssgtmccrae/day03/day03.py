"""
Ryan McGregor, 02Dec2021
AOC2021:Day03
https://adventofcode.com/2021/day/3
"""

import sys

# test_set = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

class DiagnosicReport():
    """
    Handle diagnositc repors provided during initialization.
    Input: List of Binary valid 5 digit numbers.
    """
    diag_report = []

    def __init__(self, diag_report):
        if not isinstance(diag_report, list) or len(diag_report) < 1:
            raise ValueError('diag_report should be list of similar length binary-valid numbers')
        for report in diag_report:
            set_report = set(report)
            possible_values = {'0','1'}
            if not (len(report) == len(diag_report[0]) and
                    (set_report == possible_values or set_report in possible_values)):
                raise ValueError(f'items in diag_report should be similar length binary-valid numbers, {report} is invalid')
        self.diag_report = diag_report

    def process_gamma_binary(self):
        """
        Processes gamma binary value from diag report per Day03_pt1.
        Can be XOR'd to provide epsilon binary value.
        Input: None
        Output: gamma (binary-valid string)
        """
        gamma_binary = []
        diag_counts = [0] * len(self.diag_report[0])
        for report in self.diag_report:
            for diag_report_idx, char in enumerate(report):
                diag_counts[diag_report_idx] += int(char)
        for alpha in diag_counts:
            if alpha > len(self.diag_report) / 2:
                gamma_binary.append('1')
            else:
                gamma_binary.append('0')
        return ''.join(gamma_binary)

    def process_gas_processor_rating(self, gas_type: str):
        """
        Processes o2 generator rating or co2 scrubber rating (based on input) from diag report per Day03_pt2
        Input: gas_type (str in ['o2','co2'])
        Output: rating (binary-valid string)
        """
        diag_report = self.diag_report.copy()

        gas_types = {
            'o2': {
                'alpha': '1',
                'beta': '0'
            },
            'co2': {
                'alpha': '0',
                'beta': '1'
            }
        }

        for report_char_idx in range(len(diag_report[0])):
            val = 0
            if len(diag_report) > 1:
                for item in diag_report:
                    match item[report_char_idx]:
                        case '0':
                            val -= 1
                        case '1':
                            val += 1
                if val >= 0:
                    diag_report = [x for x in diag_report if x[report_char_idx] == gas_types[gas_type]['alpha']]
                else:
                    diag_report = [x for x in diag_report if x[report_char_idx] == gas_types[gas_type]['beta']]
        return diag_report[0]

    @property
    def gamma(self):
        """Returns 'gamma' power value from provided diag_report"""
        return(int(self.process_gamma_binary(),2))


    @property
    def epsilon(self):
        """Returns 'epsilon' (XOR gamma) power value from provided diag_report"""
        mask = '1' * len(self.diag_report[0])
        return(int(self.process_gamma_binary(),2) ^ int(mask, 2))

    @property
    def o2_generator_rating(self):
        """Returns 02 Generator rating from provided diag_report"""
        return int(self.process_gas_processor_rating('o2'), 2)

    @property
    def co2_scrubber_rating(self):
        """Returns C02 Scrubber rating from provided diag_report"""
        return int(self.process_gas_processor_rating('co2'), 2)

if __name__ == '__main__':
    test_set_file = sys.argv[1]
    with open(test_set_file, 'r', encoding="utf-8") as file:
        test_set = file.read().split('\n')
    for test_set_idx, string in enumerate(test_set):
        if string == '':
            test_set.pop(test_set_idx)
    diagnostic = DiagnosicReport(test_set)
    print(f'Gamma: {diagnostic.gamma}')
    print(f'Epsilon: {diagnostic.epsilon}')
    print(f'O2: {diagnostic.o2_generator_rating}')
    print(f'CO2: {diagnostic.co2_scrubber_rating}')
