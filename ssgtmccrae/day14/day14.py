"""
Ryan McGregor, 21Dec2021
AOC2021:Day14
https://adventofcode.com/2021/day/14
"""

import cProfile
from pprint import pprint
from aocd import get_data

TEST_SET_RAW = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

class PolymerChain():
    """
    Class to manage a Polymer chain object and support iteration on it.
    Input: starting_chain (str)
    """
    starting_chain = ''
    polymer_legend = {}

    def __init__(self, starting_chain, polymer_legend):
        self.polymer_chain = starting_chain
        for pair in polymer_legend:
            pair = pair.split(' -> ')
            self.polymer_legend[pair[0]] = pair[1]

    def iterate_polymer(self, num_iterations=1):
        """
        Iterates polymer chain based on legend num_iterations number of times.
        Input: num_iterations (int)
        Output: self.polymer_chain
        """
        for iter in range(num_iterations):
            print(f'Iteration: {iter}')
            new_chain = ''
            # chain_length = int(len(self.polymer_chain))
            # current_idx = 0
            # while current_idx < chain_length:
            for idx, val in enumerate(range(int(len(self.polymer_chain)))):
                # new_chain += self.__find_polymer(current_idx)
                new_chain += self.__find_polymer(idx)
                # current_idx += 1
            self.polymer_chain = new_chain
        return self.polymer_chain


            # for idx, pair in enumerate(self.polymer_chain):
            #     string = self.polymer_chain[idx:idx+2]
            #     if len(string) == 2:
            #         if string in self.polymer_legend.keys():
            #             new_chain += f'{list(string)[0]}{self.polymer_legend[string]}'
            #         else:
            #             new_chain += {list(string)[0]}
            #     else:
            #         new_chain += list(string)[0]
            # self.polymer_chain = new_chain

    def __find_polymer(self, pos):
        str_1 = self.polymer_chain[pos:pos+2]
        if str_1 in self.polymer_legend:
            return str_1[0] + self.polymer_legend[str_1]
        return str_1[0]


if __name__ == '__main__':
    ## Testset
    starting_chain = [x for x in TEST_SET_RAW.split('\n') if x != '' and '->' not in x][0]
    legend_list = [x for x in TEST_SET_RAW.split('\n') if x != '' and '->' in x]
    ## Dataset
    # legend_list = [x for x in get_data(year=2021, day=14).split('\n') if x != '' and '->' in x]
    # starting_chain = [x for x in get_data(year=2021, day=14).split('\n') if x != '' and '->' not in x][0]

    # Pt1
    polymer_chain_1 = PolymerChain(starting_chain, legend_list)

    ## Profiling code
    cProfile.run('polymer_chain_1.iterate_polymer(20)')
    # W/O Multiproc, While loop, 3.110 seconds to 20, 106.593 seconds to 25
    # W/O Multiproc, For loop, 2.891 seconds to 20, 99.425 seconds to 25

    # polymer_string = polymer_chain_1.iterate_polymer(10)
    # element_dict = {}
    # for element in polymer_string:
    #     if element not in element_dict:
    #         element_dict[element] = 0
    #     element_dict[element] += 1
    # print('Part 1 Totals')
    # pprint(element_dict)

    # # Pt2
    # polymer_chain_2 = PolymerChain(starting_chain, legend_list)
    # polymer_string = polymer_chain_2.iterate_polymer(40)
    # element_dict = {}
    # for element in polymer_string:
    #     if element not in element_dict:
    #         element_dict[element] = 0
    #     element_dict[element] += 1
    # print('Part 2 Totals')
    # pprint(element_dict)
    # print(f'Min: {min(element_dict.values)}')
    # print(f'Max: {max(element_dict.values)}')

    # pprint([x for x in get_data(year=2021, day=14).split('\n') if x != '' and '->' in x])
    # starting_string = ([x for x in get_data(year=2021, day=14).split('\n') if x != '' and '->' not in x][0])
