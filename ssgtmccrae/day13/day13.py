"""
Ryan McGregor, 18Dec2021
AOC2021:Day11
https://adventofcode.com/2021/day/11
"""

from pprint import pprint
from aocd import get_data
import numpy as np

class TransparencyPaper():
    """
    Manages a transpaency paper object, a large (x > 1000 matrix),
    and folds along a specific axis at specific points.
    Input:
      - fold_points (list of strings containing axis and fold point)
      - dots (list of strings containing coordinates)
    """
    paper = None
    dots = []
    fold_points = []
    queued_folds = []
    max_x = 0
    max_y = 0

    def __init__(self, fold_points, dots):
        # Clean dots
        dots_list = [x.replace('()', '').split(',') for x in dots]
        for dot in dots_list:
            dot.reverse()
            self.dots.append(tuple([int(x) for x in dot]))
        # Clean fold_points
        self.queued_folds = [tuple(x.split(',')) for x in fold_points]
        # Find dimesions of paper
        self.max_x = max([int(x[0]) for x in self.dots])
        self.max_y = max([int(y[1]) for y in self.dots])
        # Create paper
        self.paper = np.zeros((self.max_x + 1,self.max_y + 1), int)
        # Place Dots
        for dot in self.dots:
            self.paper[dot] = 1

    def fold_paper(self, folds=[]):
        """
        Fold dimensions of 'paper' and line up dots.
        Input: folds (list of fold point tuples containing axis and fold point)
        Output: None
        """
        for fold in folds:








if __name__ == '__main__':

    dots_raw = ([x for x in get_data(year=2021, day=13).split('\n') if 'fold' not in x and x != ''])
    fold_points_raw = ([x.lstrip('fold along') for x in get_data(year=2021, day=13).split('\n') if 'fold' in x])
    transparency_paper = TransparencyPaper(fold_points=fold_points_raw, dots=dots_raw)
    # pprint(transparency_paper.dots)
    # pprint(transparency_paper.fold_points)
    pprint(transparency_paper.paper)
