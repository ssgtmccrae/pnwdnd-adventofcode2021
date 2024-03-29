"""
Ryan McGregor, 15Dec2021
AOC2021:Day09
https://adventofcode.com/2021/day/9
"""

from collections import namedtuple
# from pprint import pprint
from aocd import get_data
import numpy as np

TEST_SET_RAW = '''2199943210
3987894921
9856789892
8767896789
9899965678'''
test_set = []
for line in TEST_SET_RAW.split('\n'):
    test_set.append(list(line))
test_set = np.array(test_set, int)

class TopoMap():
    """
    Maintains a topo map object based on a provided numpy array.
    Input: topomap (numpy.array)
    """

    Point = namedtuple('Point', ('idx','value','risk'))

    topomap = None

    def __init__(self, _topomap):
        if isinstance(_topomap, np.ndarray):
            self.topomap = _topomap

    def north(self, idx):
        """
        Retrieves point stats for point north of idx on topomap.
        Input: valid idx tuple
        Output: Point namedtuple
        """
        if idx[0] != 0:
            north_value = self.topomap[(idx[0]-1,idx[1])]
            north_idx = (idx[0]-1,idx[1])
            return self.Point(idx=north_idx, value=int(north_value), risk=int(north_value+1))
        return None

    def south(self, idx):
        """
        Retrieves point stats for point south of idx on topomap.
        Input: valid idx tuple
        Output: Point namedtuple
        """
        if idx[0] < self.topomap.shape[0] - 1:
            south_value = self.topomap[(idx[0]+1,idx[1])]
            south_idx = (idx[0]+1,idx[1])
            return self.Point(idx=south_idx, value=int(south_value), risk=int(south_value+1))
        return None

    def east(self, idx):
        """
        Retrieves point stats for point east of idx on topomap.
        Input: valid idx tuple
        Output: Point namedtuple
        """
        if idx[1] < self.topomap.shape[1] - 1:
            east_value = self.topomap[(idx[0],idx[1]+1)]
            east_idx = (idx[0],idx[1]+1)
            return self.Point(idx=east_idx, value=int(east_value), risk=int(east_value+1))
        return None

    def west(self, idx):
        """
        Retrieves point stats for point west of idx on topomap.
        Input: valid idx tuple
        Output: Point namedtuple
        """
        if idx[1] != 0:
            west_value = self.topomap[(idx[0],idx[1]-1)]
            west_idx = (idx[0],idx[1]-1)
            return self.Point(idx=west_idx, value=int(west_value), risk=int(west_value+1))
        return None

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
        for idx, value in np.ndenumerate(self.topomap):
            # print(f'idx: {idx}, value: {value}')
            north,south,east,west = self.north(idx), self.south(idx), self.east(idx), self.west(idx)
            # print(f'n:{n}, s:{s}, e:{e}, w:{w}')
            if len([x.value for x in [north,south,east,west] if x is not None and x.value <= value ]) == 0:
                lowpoints.append(self.Point(idx=idx, value=int(value), risk=int(value+1)))
        return lowpoints

    @property
    def basins(self):
        """
        Recursively finds members of a basin surrounded by max height points.
        This is a bloody hack due to the thinking I'd have to find how to teach a compute what a ridgeline is...
        Somehow I hate this more.
        Input: None
        Output: list of Basin objects (defined below)
        """
        Basin = namedtuple('Basin', ('lowpoint','points'))
        basins = []
        for lowpoint in self.lowpoints:
            basin_members = []
            # print(f'lowpoint: {lowpoint}')
            self.__find_basin_members(lowpoint, basin_members)
            basins.append(Basin(lowpoint=lowpoint, points=basin_members))
        return basins

    def __find_basin_members(self, point, basin_members):
        """Recursive operator for self.basins"""
        if point.value != 9:
            basin_members.append(point)
            neighbors = [x for x in [self.north(point.idx), self.south(point.idx), self.east(point.idx), self.west(point.idx)] if x is not None]
            # print(f'point: {point}, neighbors: {neighbors}, basin_members: {basin_members}')
            for neighbor in neighbors:
                # print(f'neighbor: {neighbor}')
                # pprint([x.idx for x in basin_members])
                if neighbor.idx not in [x.idx for x in basin_members]:
                    # print(f'recusing for {neighbor}')
                    self.__find_basin_members(neighbor, basin_members)


if __name__ == '__main__':
    # topomap = TopoMap(test_set) # Test Code
    dataset = []
    for line in get_data(year=2021, day=9).split('\n'):
        dataset.append(list(line))
    dataset = np.array(dataset, int)
    topomap = TopoMap(dataset)

    # Part 1
    print(f'Pt1 - Total Risk: {topomap.total_risk}')

    # Part 2
    basin_list = topomap.basins
    basin_list.sort(key=lambda x: len(x.points), reverse=True)
    print(f'Pt2 - Product of size of 3 largest basins: {np.prod([len(x.points) for x in basin_list[:3]])}')
