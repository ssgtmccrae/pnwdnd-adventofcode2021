
"""
Ryan McGregor, 01Dec2021
AOC2021:Day02
https://adventofcode.com/2021/day/2
"""

from pprint import pprint
from typing import List
import sys

class Submarine():
    """
    Object to manage the y/z coorinates of a submarine based on a list of orders.
    Input: List of orders ([(direction, distance)])
    """
    pos_y = 0
    pos_z = 0

    def __init__(self, move_orders: List[tuple]):
        self.validate_orders(move_orders)
        self.move_submarine(move_orders)

    def validate_orders(self, move_orders):
        if type(move_orders) != list:
            raise ValueError("'move_orders' must be a list of tuples")
        for move in move_orders:
            if (type(move) != tuple
                or len(move) != 2
                or type(move[0]) != str
                or move[0] not in ['up','down','forward']
                or type(int(move[1])) != int):
                print(f'{move} not valid')
                raise ValueError("'move_orders' should be a list of tuples containing a direction (up,down,forward) and a distance")

    def move_submarine(self, move_orders):
        for order in move_orders:
            match order[0]:
                case 'up':
                    self.pos_z -= int(order[1])
                case 'down':
                    self.pos_z += int(order[1])
                case 'forward':
                    self.pos_y += int(order[1])

if __name__ == '__main__':
    test_set_file = sys.argv[1]
    with open(test_set_file, 'r', encoding="utf-8") as file:
        test_set = file.read().split('\n')
    for idx, string in enumerate(test_set):
        if string != '':
            test_set[idx] = tuple(string.split(' '))
        else:
            test_set.pop(idx)
    submarine = Submarine(test_set)
    print(f'File Analyzed: {test_set_file}')
    print(f'Y Pos: {submarine.pos_y}')
    print(f'Z Pos: {submarine.pos_z}')

