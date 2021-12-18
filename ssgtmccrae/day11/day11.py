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
test_set = np.array([list(x) for x in TEST_SET_RAW.split('\n') if x != ''], int)
# 100 Steps, 1656 Flashes

class OctopusGraph():
    """
    Manages a group of Octopi and determines their current state based on number of times flashed.
    Contains counters for numbers of flashes.
    """

    state = None
    cycles_ticked: 0

    def __init__(self, starting_state: np.ndarray):
        if isinstance(starting_state, np.ndarray):
            self.state = starting_state

    def tickState(self, number_of_cycles=1):
        """
        Tick state of the Octopus field.
        Input: number_of_cycles (int, default: 1)
        Output: None
        """
        pprint(self.state)
        for x in range(int(number_of_cycles)):
            self.state = np.add(self.state, np.ones(shape=self.state.shape, dtype=int))
            flash_mask = np.ones(self.state.shape)
            for idx, value in np.ndenumerate(self.state):
                if flash_mask[idx] * self.state[idx] > 9:
                    self.__flashPoint(idx, flash_mask)
            pprint(self.state)

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

    # def __flashPoint(self, point):





if __name__ == '__main__':
    dataset = get_data(year=2021, day=11).split('\n')
    octopus_field = OctopusGraph(np.array(test_set, int))
    pprint(octopus_field.state)
    surroundings_1 = octopus_field.getSurroundings((1,1))
    for direction in surroundings_1:
        print(f'point: {direction}, value: {octopus_field.state[surroundings_1[direction]]}')
    pprint(octopus_field.state)
    surroundings_2 = octopus_field.getSurroundings((0,0))
    for direction in surroundings_2:
        print(f'point: {direction}, value: {octopus_field.state[surroundings_2[direction]]}')
