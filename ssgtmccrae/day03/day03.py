"""
Ryan McGregor, 02Dec2021
AOC2021:Day03
https://adventofcode.com/2021/day/3
"""

from typing import List
import sys

# test_set = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

class DiagnosicReport():
    """
    Handle diagnositc repors provided during initialization.
    Input: List of Binary valid 5 digit numbers.
    """
    diag_report = []
    gamma_binary = []

    def __init__(self, diag_report):
        self.validate_diag_report(diag_report)
        self.diag_report = diag_report
        self.process_gamma_binary()

    def validate_diag_report(self, diag_report):
        """
        Validates diag_report
        Input: diag_report (List[str])
        """
        if not isinstance(diag_report, list) or len(diag_report) < 1:
            raise ValueError('diag_report should be list of similar length binary-valid numbers')
        for x in diag_report:
            set_x = set(x)
            possible_values = {'0','1'}
            if not (len(x) == len(diag_report[0]) and
                    (set_x == possible_values or set_x in possible_values)):
                raise ValueError(f'items in diag_report should be similar length binary-valid numbers, {x} is invalid')

    def process_gamma_binary(self):
        """
        Processes gamma binary value from diag report per Day03_pt1
        Input: None
        Output: None
        """
        gamma_binary = []
        diag_counts = [0] * len(self.diag_report[0])
        for item in self.diag_report:
            for idx, x in enumerate([x for x in item]):
                diag_counts[idx] += int(x)
        for x in diag_counts:
            if (x > len(self.diag_report) / 2):
                gamma_binary.append('1')
            else:
                gamma_binary.append('0')
        self.gamma_binary =  ''.join(gamma_binary)

    def process_gen_scrubber_rating(self, gas_type):
        """
        Processes o2 generator rating from diag report per Day03_pt2
        Input: None
        Output: None
        """
        diag_report = self.diag_report.copy()

        match gas_type:
            case 'o2':
                alpha = '1'
                beta = '0'
            case 'co2':
                alpha = '0'
                beta = '1'

        for idx, iter in enumerate(range(len(diag_report[0]))):
            val = 0
            if len(diag_report) > 1:
                for item in diag_report:
                    match item[idx]:
                        case '0':
                            val -= 1
                        case '1':
                            val += 1
                if val >= 0:
                    diag_report = [x for x in diag_report if x[idx] == alpha]
                else:
                    diag_report = [x for x in diag_report if x[idx] == beta]
        return int(diag_report[0],2)

    @property
    def gamma(self):
        """Returns 'gamma' power value from provided diag_report"""
        return(int(self.gamma_binary,2))

    @property
    def epsilon(self):
        """Returns 'epsilon' (XOR gamma) power value from provided diag_report"""
        mask = '1' * len(self.diag_report[0])
        return(int(self.gamma_binary,2) ^ int(mask, 2))

    @property
    def o2_generator_rating(self):
        """Returns 02 Generator rating from provided diag_report"""
        return(self.process_gen_scrubber_rating('o2'))

    @property
    def co2_scrubber_rating(self):
        """Returns C02 Scrubber rating from provided diag_report"""
        return(self.process_gen_scrubber_rating('co2'))

if __name__ == '__main__':
    test_set_file = sys.argv[1]
    with open(test_set_file, 'r', encoding="utf-8") as file:
        test_set = file.read().split('\n')
    for idx, string in enumerate(test_set):
        if string == '':
            test_set.pop(idx)
    diagnostic = DiagnosicReport(test_set)
    print(f'Gamma: {diagnostic.gamma}')
    print(f'Epsilon: {diagnostic.epsilon}')
    print(f'O2: {diagnostic.o2_generator_rating}')
    print(f'CO2: {diagnostic.co2_scrubber_rating}')
