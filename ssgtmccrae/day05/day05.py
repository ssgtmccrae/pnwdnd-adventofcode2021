
"""
Ryan McGregor, 04Dec2021
AOC2021:Day05
https://adventofcode.com/2021/day/5
"""

from pprint import pprint
import sys
import numpy as np

test_set = [
[(0,9),(5,9)],
[(8,0),(0,8)],
[(9,4),(3,4)],
[(2,2),(2,1)],
[(7,0),(7,4)],
[(6,4),(2,0)],
[(0,9),(2,9)],
[(3,4),(1,4)],
[(0,0),(8,8)],
[(5,5),(8,2)]]

# class CoordinateGrid():
#     """
#     Manages a coordinate grid, lines on that grid, and a heat graph for number of intersecting horizontal and vertical lines.
#     Input: coords_list (List[List[tuple(int,int)]])
#     """
#     grid = None
#     coords_list = []

#     def __init__(self, grid_size, coords_list):

def determineIntersects(grid_size, coord_list):
    grid = np.zeros((grid_size, grid_size))
    for coord_pair in coord_list:
        # [(777,778),(777,676)]

        pprint(coord_pair)
        if coord_pair[0][0] == coord_pair[1][0]:
            # X axis remains constant, draw y-axis line
            limits = (int(coord_pair[0][1]),int(coord_pair[1][1]))
            for y in range(min(limits), max(limits) + 1):
                grid[int(coord_pair[0][0]), int(y)] += 1
        elif coord_pair[0][1] == coord_pair[1][1]:
            # Y axis remains constant, draw x-axis line
            limits = (int(coord_pair[0][0]),int(coord_pair[1][0]))
            for x in range(min(limits), max(limits) + 1):
                grid[int(x), int(coord_pair[0][1])] += 1
        # else:
        #     raise ValueError(f'WARNING: Diagonal path detected. {coord_pair}')
    pprint(grid)
    intersects_array = np.where(grid >= 2)
    intersects_list = []
    for idx in range(len(intersects_array[0].tolist())):
        intersects_list.append((intersects_array[0].tolist()[idx], intersects_array[1].tolist()[idx]))
    pprint(intersects_list)
    print(len(intersects_list))


if __name__ == '__main__':
    coords_file = sys.argv[1]
    coords = []
    # Clean data from bingo cards file
    with open(coords_file, 'r', encoding="utf-8") as file:
        for line in file.read().split('\n'):
            if line != '':
                coord_pair = []
                for coord in line.split(' '):
                    coord_pair.append(tuple(coord.strip('()').split(',')))
                coords.append(coord_pair)
    determineIntersects(grid_size=1000, coord_list=coords)
