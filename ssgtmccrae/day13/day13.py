"""
Ryan McGregor, 18Dec2021
AOC2021:Day11
https://adventofcode.com/2021/day/11
"""

from pprint import pprint
from aocd import get_data
import numpy as np

TEST_SET = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

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
    max_x = 0
    max_y = 0

    def __init__(self, dots):
        # Clean dots
        dots_list = [x.replace('()', '').split(',') for x in dots]
        for dot in dots_list:
            dot.reverse()
            self.dots.append(tuple([int(x) for x in dot]))
        # Find dimesions of paper
        self.max_x = max([int(x[0]) for x in self.dots])
        self.max_y = max([int(y[1]) for y in self.dots])
        # Create paper
        self.paper = np.zeros((self.max_x + 1,self.max_y + 1), bool)
        # Place Dots
        for dot in self.dots:
            self.paper[dot] = True

    def fold_paper(self, folds):
        """
        Fold dimensions of 'paper' and line up dots.
        Input: folds (list of fold point tuples containing axis and fold point)
        Output: None
        """
        for fold in folds:
            print('Before')
            pprint(self.paper)
            print(f'Folding: {fold}')
            if fold[0] == 'x':
                self.paper = np.swapaxes(self.paper,0,1)
                self.paper = np.fliplr(self.paper)
            part_1, _ , part_2 = np.split(self.paper, [fold[1], (fold[1]+1)], 0)
            if part_1.size >= part_2.size:
                part_1 = np.flip(part_1, axis=0)
                for idx, _ in np.ndenumerate(part_2):
                    part_1[idx] = np.logical_or(part_1[idx], part_2[idx])
                part_1 = np.flip(part_1, axis=0)
            self.paper = part_1
            if fold[0] == 'x':
                self.paper = np.fliplr(self.paper)
                self.paper = np.swapaxes(self.paper,0,1)


if __name__ == '__main__':
    # dots_raw = ([x for x in TEST_SET.split('\n') if 'fold' not in x and x != ''])
    dots_raw = ([x for x in get_data(year=2021, day=13).split('\n') if 'fold' not in x and x != ''])
    fold_points_raw = ([x.lstrip('fold along') for x in get_data(year=2021, day=13).split('\n') if 'fold' in x])
    fold_points = [tuple([x.split('=')[0], int(x.split('=')[1])]) for x in fold_points_raw]

    ## Pt 1
    transparency_paper_pt1 = TransparencyPaper(dots=dots_raw)
    transparency_paper_pt1.fold_paper([('x',655)])
    print('Part 1 Answer')
    print(list(transparency_paper_pt1.paper.flat).count(True))

    ## Pt 2
    transparency_paper_pt2 = TransparencyPaper(dots=dots_raw)
    transparency_paper_pt2.fold_paper(fold_points)

    print('Part 2 Answer')
    for line in transparency_paper_pt2.paper.tolist():
        line_list = []
        for char in line:
            match char:
                case True:
                    line_list.append('x')
                case False:
                    line_list.append(' ')
        print(''.join(line_list))
