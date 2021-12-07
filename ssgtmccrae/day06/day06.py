"""
Ryan McGregor, 05Dec2021
AOC2021:Day06
https://adventofcode.com/2021/day/6
"""
from pprint import pprint
import sys
import numpy as np

def run_counter(generations: int, starting_set: list[int]):
    """
    Runs a counter for 'generations' number of events, where each item in starting_set' spawns a child
    which will produce another child in 8 days.
    Input: generations (int), starting_set (List(int))
    Output: dict containing counters for each 'time_to_breed'
    """
    counter = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    for number in starting_set:
        counter[int(number)] += 1

    print('Initial state:')
    pprint(counter)

    current_gen = 0
    while current_gen < generations:
        for key in counter.keys():
            if key == 0:
                counter[9] = counter[0]
                counter[7] += counter[0]
            if key <= 8:
                counter[key] = counter[key + 1]
        counter[9] = 0
        current_gen += 1
        print(f'gen: {current_gen}')
        pprint(counter)
    return counter


if __name__ == '__main__':
    dataset = []
    ages_file, generations = sys.argv[1], sys.argv[2]
    # Clean data from bingo cards file
    with open(ages_file, 'r', encoding="utf-8") as file:
        for line in file.read().split('\n'):
            if line != '':
                for num in line.split(','):
                    dataset.append(num)
    # dataset = [3,4,3,1,2] # = 5934 w/ gen=80 or 26984457539 w/ gen=256
    counter = run_counter(int(generations), dataset)
    print(f'Total Fish: {sum(counter.values())}')
    pprint(counter)
