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
import time

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

class PolymerChain():
    """
    Manages polymer chain counters, allows for iteration based on provided polymer legend.
    Input: polymer_chain (str), polymer_legend (dict)
    """
    polymer_legend = {}
    polymer_chain = {}
    polymer_totals = {}
    def __init__(self, polymer_chain, polymer_legend):
        self.polymer_legend = polymer_legend
        for idx in range(len(polymer_chain)):
            if polymer_chain[idx] not in self.polymer_totals:
                self.polymer_totals[polymer_chain[idx]] = 0
            self.polymer_totals[polymer_chain[idx]] += 1
            pair = polymer_chain[idx:idx+2]
            if len(pair) == 2:
                if pair not in self.polymer_chain:
                    self.polymer_chain[pair] = 0
                self.polymer_chain[pair] += 1

    def iterate_polymer(self, num_iterations=1):
        """
        Iterates polymer chain based on legend num_iterations number of times.
        Input: num_iterations (int)
        Output: self.polymer_chain
        """
        for iter in range(num_iterations):
            new_chain = {}
            for pair in self.polymer_chain:
                if self.polymer_legend[pair] not in self.polymer_totals:
                    self.polymer_totals[self.polymer_legend[pair]] = 0
                self.polymer_totals[self.polymer_legend[pair]] += self.polymer_chain[pair]
                new_pair_1 = (pair[0] + self.polymer_legend[pair], self.polymer_chain[pair])
                new_pair_2 = (self.polymer_legend[pair] + pair[1], self.polymer_chain[pair])
                for add in [new_pair_1, new_pair_2]:
                    if add[0] not in new_chain:
                        new_chain[add[0]] = 0
                    new_chain[add[0]] += add[1]
            self.polymer_chain = new_chain
        return self.polymer_chain



if __name__ == '__main__':

    # Test Set
    # RAW = TEST_SET_RAW
    # Data Set
    RAW = get_data(year=2021, day=14)

    polymer_chain = [x for x in RAW.split('\n') if x != '' and '->' not in x][0]
    polymer_legend = {}
    for pair in [x.split(' -> ') for x in RAW.split('\n') if x != '' and '->' in x]:
        polymer_legend[pair[0]] = pair[1]

    ## Pt1
    polymer = PolymerChain(polymer_chain, polymer_legend)
    print(polymer.iterate_polymer(10))
    print('Part 1 Totals')
    pprint(f'{polymer.polymer_totals}')
    print(f'Min: {min(polymer.polymer_totals.values())}')
    print(f'Max: {max(polymer.polymer_totals.values())}')
    print(f'Answer Value: {max(polymer.polymer_totals.values()) - min(polymer.polymer_totals.values())}')

    # Pt2
    print(polymer.iterate_polymer(30))
    print('Part 2 Totals')
    pprint(f'{polymer.polymer_totals}')
    print(f'Min: {min(polymer.polymer_totals.values())}')
    print(f'Max: {max(polymer.polymer_totals.values())}')
    print(f'Answer Value: {max(polymer.polymer_totals.values()) - min(polymer.polymer_totals.values())}')
