"""
Ryan McGregor, 05Dec2021
AOC2021:Day06
https://adventofcode.com/2021/day/6
"""
from pprint import pprint
import sys

def run_counter(_generations: int, starting_set: list[int]):
    """
    Runs a _counter for '_generations' number of events, where each item in starting_set' spawns a child
    which will produce another child in 8 days.
    Input: _generations (int), starting_set (List(int))
    Output: dict containing _counters for each 'time_to_breed'
    """
    _counter = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    for number in starting_set:
        _counter[int(number)] += 1

    print('Initial state:')
    pprint(_counter)

    current_gen = 0
    while current_gen < _generations:
        for key in sorted(_counter):
            if key == 0:
                _counter[9] = _counter[0]
                _counter[7] += _counter[0]
            if key <= 8:
                _counter[key] = _counter[key + 1]
        _counter[9] = 0
        current_gen += 1
        print(f'gen: {current_gen}')
        pprint(_counter)
    return _counter


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
