"""
Ryan McGregor, 25Dec2021
AOC2021:Day15
https://adventofcode.com/2021/day/15
"""

from pprint import pprint
from aocd import get_data
import numpy as np

TEST_SET_RAW = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

def find_path(grid):
    """
    Use an A* similar algorithm to the find the path through a grid with the lowest possible cost.
    Input: grid (np.array), start (index tuple), end (index tuple)
    Output: shortest_path (List of nodes), total_cost (int)
    """


if __name__ == '__main__':
    # Test Set
    RAW = TEST_SET_RAW
    # Data Set
    # RAW = get_data(year=2021, day=15)
    processed_raw = np.array([list(x) for x in RAW.split('\n')])
    pprint(processed_raw)
