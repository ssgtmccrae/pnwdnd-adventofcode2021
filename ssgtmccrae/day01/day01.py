"""
Ryan McGregor, 01Dec2021
AOC2021:Day01
https://adventofcode.com/2021/day/1
"""

from typing import List
import sys

class DepthSet():
    """
    Object to contain a depth set and provide information on that depth set such as time_increased, times_decreased, highest and lowest.
    Input: List(int) of depths
    Output: None
    """

    depth_set = []
    depth_deltas = []

    def __init__(self, depth_set: List[int]):
        if len(depth_set) < 2:
            raise ValueError('depth_set must contain more than one depth.')
        self.depth_set = [int(depth) for depth in depth_set]
        self.check_deltas()

    def check_deltas(self):
        """
        Checks the difference between a depth and the one immediately after it and appends that to a list.
        Input: self.depth_set (List[int])
        Output: self.depth_deltas (List[int])
        """
        depth_set = self.depth_set.copy()
        depth_deltas = []
        # 'For' loop does not work due to final index or first index being invalid.
        # List of deltas by nature must be one less than original list.
        while len(depth_set) > 1:
            # Simultaneously performs required math and removes first list item.
            depth_deltas.append(depth_set[1]-depth_set.pop(0))
        self.depth_deltas = depth_deltas

    @property
    def increases(self):
        """
        Getter to list number of times depth increases from its previous value.
        Input: self.depth_deltas (List[int])
        Output: int
        """
        return len([delta for delta in self.depth_deltas if delta > 0])

    @property
    def decreases(self):
        """
        Getter to list number of times depth decreases from its previous value.
        Input: self.depth_deltas (List[int])
        Output: int
        """
        return len([delta for delta in self.depth_deltas if delta < 0])

# ## Test Code
# test_set = [199,200,208,210,200,207,240,269,260,263]
# depthset = DepthSet(test_set)
# print(depthset.increases) # 7
# print(depthset.decreases) # 2

if __name__ == '__main__':
    test_set_file = sys.argv[1]
    with open(test_set_file, 'r', encoding="utf-8") as file:
        test_set = file.read().split()
    depthset = DepthSet(test_set)
    print(f'File Analyzed: {test_set_file}')
    print(f'Number of increases: {depthset.increases}')
    print(f'Number of decreases: {depthset.decreases}')
