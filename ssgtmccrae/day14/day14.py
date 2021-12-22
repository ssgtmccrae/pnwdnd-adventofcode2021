"""
Ryan McGregor, 21Dec2021
AOC2021:Day14
https://adventofcode.com/2021/day/14
"""

import cProfile
from pprint import pprint
from aocd import get_data
import numpy as np
import multiprocessing as mp

NUM_CORES = 20

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

def __find_polymer(pos, current_chain, polymer_legend):
    str_1 = current_chain[pos:pos+2]
    if str_1 in polymer_legend:
        chunk = str_1[0] + polymer_legend[str_1]
    else:
        chunk = str_1[0]
    return chunk

def iterate_polymer(current_chain, polymer_legend, num_iterations=1):
    """
    Iterates polymer chain based on legend num_iterations number of times.
    Input: num_iterations (int)
    Output: self.polymer_chain
    """
    ## String Concat
    for iter in range(num_iterations):
        new_chain = ''
        print(f'Iteration: {iter}')
        for idx in range(len(current_chain)):
            new_chain += __find_polymer(idx, current_chain, polymer_legend)
        current_chain = new_chain
    return polymer_chain

    # ## Array Sequencing/Joining (No MiltiProc)
    # for iter in range(num_iterations):
    #     chain_length = len(self.polymer_chain)
    #     new_chain = np.zeros((chain_length * 2), dtype=str)
    #     print(f'Iteration: {iter}')
    #     for idx in range(chain_length):
    #         self.__find_polymer(idx, new_chain)
    #     self.polymer_chain = new_chain[new_chain.nonzero()]
    # return self.polymer_chain

    # ## Array Sequencing/Joining (MULTIPROCESSING!)
    # pool = mp.Pool(processes=NUM_CORES)

    # for iter in range(num_iterations):
    #     print(f'Iteration: {iter}')
    #     chain_length = len(current_chain)
    #     results = [pool.apply_async(__find_polymer, args=(idx, current_chain, polymer_legend)) for idx in range(chain_length)]
    #     new_chain_unsorted = [p.get() for p in results]
    #     new_chain_dict = {}
    #     for item in new_chain_unsorted:
    #         new_chain_dict[item[0]] = item[1]
    #     new_chain = ''
    #     for idx in range(len(new_chain_dict)):
    #         new_chain += new_chain_dict[idx]
    #     current_chain = new_chain
    # return current_chain


if __name__ == '__main__':

    # Test Set
    RAW = TEST_SET_RAW
    # Data Set
    # RAW = get_data(year=2021, day=14)

    polymer_chain = [x for x in RAW.split('\n') if x != '' and '->' not in x][0]
    polymer_legend = {}
    for pair in [x.split(' -> ') for x in RAW.split('\n') if x != '' and '->' in x]:
        polymer_legend[pair[0]] = pair[1]

    ## Profiling code
    # USING TESTSET!
    # cProfile.run('iterate_polymer(polymer_chain, polymer_legend, num_iterations=20)')
    # cProfile.run('polymer_chain_1.iterate_polymer(25)')
    # W/O Multiproc, While loop using string concat, 3.110 seconds to 20, 106.593 seconds to 25
    # W/O Multiproc, For loop using string concat, 2.891 seconds to 20, 99.425 seconds to 25
    # W/O Multiproc, For loop using list append, 3.769 seconds to 20, 119.368 seconds to 25
    # W/O Multiproc, For loop using string_concat final, 2.758 seconds to 20, 87.687 seconds to 25
    # W/ Multiproc, For loop using list return (async) to dict sort... Untennable. 20-50x slower.
    # Personal note: I really wish that Multiproc was worth it. the code works, produces reliable x10 result
    #                but this problem is just WAY fast as a string concat problem. ¯\_(ツ)_/¯

    # ## Pt1
    # polymer_string = iterate_polymer(polymer_chain, polymer_legend, num_iterations=10)
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
