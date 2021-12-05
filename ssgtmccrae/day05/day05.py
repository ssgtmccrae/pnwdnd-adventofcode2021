
"""
Ryan McGregor, 04Dec2021
AOC2021:Day05
https://adventofcode.com/2021/day/5
"""

from pprint import pprint
import sys
import numpy as np

def determine_intersects(grid_size, coord_list):
    """
    Determins intersection points > strength 1, on the assumption that all lines are either vertical, horizontal, or 45deg
    using a Numpy array.
    Input: grid_size (int), coord_list (List[List[tuple(int,int)]])
    Output: None
    """
    grid = np.zeros((grid_size, grid_size))
    for coord_pair in coord_list:
        current_coord = coord_pair[0]
        while True:
            grid[current_coord] += 1
            new_coord = list(current_coord)
            for axis in [0,1]:
                if current_coord[axis] < coord_pair[1][axis]:
                    new_coord[axis] = current_coord[axis] + 1
                elif current_coord[axis] > coord_pair[1][axis]:
                    new_coord[axis] = current_coord[axis] - 1
            current_coord = tuple(new_coord)
            if current_coord == coord_pair[1]:
                grid[current_coord] += 1
                break
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
                    coord_pair.append(tuple([int(x) for x in coord.strip('()').split(',')]))
                coords.append(coord_pair)
    determineIntersects(grid_size=1000, coord_list=coords)
