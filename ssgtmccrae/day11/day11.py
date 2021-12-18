"""
Ryan McGregor, 18Dec2021
AOC2021:Day11
https://adventofcode.com/2021/day/11
"""

# from pprint import pprint
from collections import namedtuple
from aocd import get_data
from pprint import pprint
import numpy as np

TEST_SET_RAW = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

class OctopusGraph():
    """
    Manages a group of Octopi and determines their current state based on number of times flashed.
    Contains counters for numbers of flashes.
    """

    state = None
    cycles_ticked = 0
    flashes = 0

    def __init__(self, starting_state: np.ndarray):
        if isinstance(starting_state, np.ndarray):
            self.state = starting_state

    def tickState(self, number_of_cycles=1):
        """
        Tick state of the Octopus field.
        Input: number_of_cycles (int, default: 1)
        Output: None
        """
        for x in range(int(number_of_cycles)):
            self.cycles_ticked += 1
            self.state = np.add(self.state, np.ones(shape=self.state.shape, dtype=int))
            flash_mask = np.ones(self.state.shape)
            for idx, value in np.ndenumerate(self.state):
                if self.state[idx] * flash_mask[idx] > 9:
                    self.flashPoint(idx, flash_mask)
            self.state = np.multiply(self.state, flash_mask)

    def getSurroundings(self, point_idx):
        """
        Gets points surrounding a point on the OctopusGraph state array.
        Input: point_idx (tuple(int))
        Output: surroundings (dict)
        """
        COMPASS_DIRECTIONS = {
            'n': (-1, 0),
            's': (1, 0),
            'w': (0,-1),
            'e': (0, 1),
            'nw': (-1, -1),
            'sw': (1, -1),
            'ne': (-1, 1),
            'se': (1, 1),
            }
        surroundings = {}
        for direction in COMPASS_DIRECTIONS:
            if (point_idx[0] + COMPASS_DIRECTIONS[direction][0] < self.state.shape[0] and
                point_idx[0] + COMPASS_DIRECTIONS[direction][0] >= 0 and
                point_idx[1] + COMPASS_DIRECTIONS[direction][1] < self.state.shape[0] and
                point_idx[1] + COMPASS_DIRECTIONS[direction][1] >= 0):
                surroundings[direction] = (
                    point_idx[0] + COMPASS_DIRECTIONS[direction][0],
                    point_idx[1] + COMPASS_DIRECTIONS[direction][1]
                    )
        return surroundings

    def flashPoint(self, point_idx, flash_mask):
        """
        Flashes point and surrounding points.
        Input: point (tuple(int))
        Output: None
        """
        flash_mask[point_idx] = 0
        self.flashes += 1
        surroundings = self.getSurroundings(point_idx)
        for neighbor_idx in surroundings.values():
            self.state[neighbor_idx] += 1
            if self.state[neighbor_idx] * flash_mask[neighbor_idx] > 9:
                self.flashPoint(neighbor_idx, flash_mask)








if __name__ == '__main__':
    # test_set = np.array([list(x) for x in TEST_SET_RAW.split('\n') if x != ''], int)
    # octopus_field = OctopusGraph(np.array(test_set, int)) # test code, expected 1656 flashes at 100 cycles

    dataset = np.array([list(x) for x in get_data(year=2021, day=11).split('\n') if x != ''], int)
    octopus_field = OctopusGraph(dataset)
    # Pt 1
    octopus_field.tickState(100)
    print(octopus_field.flashes)
