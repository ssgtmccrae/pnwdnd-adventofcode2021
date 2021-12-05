
"""
Ryan McGregor, 03Dec2021
AOC2021:Day04
https://adventofcode.com/2021/day/4
"""

from pprint import pprint
import sys

if __name__ == '__main__':
    coords_file = sys.argv[1]
    coords_list = []
    # Clean data from bingo cards file
    with open(coords_file, 'r', encoding="utf-8") as file:
      for line in file.read().split('\n'):
        if line != '':
          coord_pair = []
          for coord in line.split(' '):
            coord_pair.append(tuple(coord.strip('()').split(',')))
          coords_list.append(coord_pair)

    pprint(coords_list)
