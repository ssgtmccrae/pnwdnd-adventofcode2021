"""
Ryan McGregor, 15Dec2021
AOC2021:Day09
https://adventofcode.com/2021/day/9
"""

from collections import namedtuple
from aocd import get_data
from pprint import pprint
import numpy as np

test_set_raw = '''2199943210
3987894921
9856789892
8767896789
9899965678'''
test_set = []
for line in test_set_raw.split('\n'):
    test_set.append(list(line))
test_set = np.array(test_set, int)

class TopoMap():
    """
    Maintains a topo map object based on a provided numpy array.
    Input: topomap (numby.array)
    """

    topomap = None

    def __init__(self, topomap):
        if isinstance(topomap, np.ndarray):
            self.topomap = topomap

    @property
    def total_risk(self):
        """
        Returns total risk score for all lowpoints across the topo map.
        Input: None
        Output: total_risk (int)
        """
        return sum([x.risk for x in self.lowpoints])

    @property
    def lowpoints(self):
        """
        Getter for low points on a topomap.
        Input: None
        Output: List of coords that are low points (List[(Coords)])
        """
        lowpoints = []
        Point = namedtuple('Point', ('idx','value','risk'))
        for idx, value in np.ndenumerate(self.topomap):
            # print(f'idx: {idx}, value: {value}')
            n,w,s,e = None, None, None, None
            if idx[0] != 0:
                n = self.topomap[(idx[0]-1,idx[1])]
            if idx[1] != 0:
                w = self.topomap[(idx[0],idx[1]-1)]
            if idx[0] < self.topomap.shape[0] - 1:
                s = self.topomap[(idx[0]+1,idx[1])]
            if idx[1] < self.topomap.shape[1] - 1:
                e = self.topomap[(idx[0],idx[1]+1)]
            # print(f'n:{n}, s:{s}, e:{e}, w:{w}')
            if len([x for x in [n,s,w,e] if x is not None and x <= value ]) == 0:
                lowpoints.append(Point(idx=idx, value=int(value), risk=int(value+1)))
        return lowpoints

if __name__ == '__main__':
    # topomap = TopoMap(test_set) # Test Code
    dataset = []
    for line in get_data(year=2021, day=9).split('\n'):
        dataset.append(list(line))
    dataset = np.array(dataset, int)
    topomap = TopoMap(dataset)
    print(topomap.total_risk)
