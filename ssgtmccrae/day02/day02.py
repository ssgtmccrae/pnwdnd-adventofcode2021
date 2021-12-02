
"""
Ryan McGregor, 01Dec2021
AOC2021:Day02
https://adventofcode.com/2021/day/2
"""

from typing import List
import sys

class SubmarinePt1():
    """
    Object to manage the y/z coorinates of a submarine based on a list of orders.
    Utilizes instructions for Part 1 of challenge.
    Input: List of orders ([(direction, distance)])
    """
    pos_y = 0
    pos_z = 0

    def __init__(self, move_orders: List[tuple]):
        self.validate_orders(move_orders)
        self.move_submarine(move_orders)

    def validate_orders(self, move_orders):
        """
        Validates move_orders as valid for use.
        Expects List of Tuples containing direction and distance.
        Input: List of Tuples (string, int)
        Output: None
        """
        if not isinstance(move_orders, list):
            raise ValueError("'move_orders' must be a list of tuples")
        for move in move_orders:
            if not (isinstance(move, tuple)
                and len(move) == 2
                and isinstance(move[0], str)
                and move[0] in ['up','down','forward']
                and isinstance(int(move[1]), int)):
                print(f'{move} not valid')
                raise ValueError("'move_orders' should be a list of tuples containing a direction (up,down,forward) and a distance")

    def move_submarine(self, move_orders):
        """
        Moves submarine per pt1 explanation.
        Input: move_orders, list of tuples (validated)
        Output: None
        """
        for order in move_orders:
            match order[0]:
                case 'up':
                    self.pos_z -= int(order[1])
                case 'down':
                    self.pos_z += int(order[1])
                case 'forward':
                    self.pos_y += int(order[1])

class SubmarinePt2(SubmarinePt1):
    """
    Object to manage the y/z coorinates of a submarine based on a list of orders.
    Utilizes instructions for Part 2 of challenge.
    Input: List of orders ([(direction, distance)])
    """
    aim = 0

    def move_submarine(self, move_orders):
        for order in move_orders:
            match order[0]:
                case 'up':
                    self.aim -= int(order[1])
                case 'down':
                    self.aim += int(order[1])
                case 'forward':
                    self.pos_y += int(order[1])
                    self.pos_z += self.aim * int(order[1])

if __name__ == '__main__':
    test_set_file = sys.argv[1]
    with open(test_set_file, 'r', encoding="utf-8") as file:
        test_set = file.read().split('\n')
    for idx, string in enumerate(test_set):
        if string != '':
            test_set[idx] = tuple(string.split(' '))
        else:
            test_set.pop(idx)
    print('Performing analysis for pt1...')
    submarine_1 = SubmarinePt1(test_set)
    print(f'File Analyzed: {test_set_file}')
    print(f'Y Pos: {submarine_1.pos_y}')
    print(f'Z Pos: {submarine_1.pos_z}')
    print('Performing analysis for pt2...')
    submarine_2 = SubmarinePt2(test_set)
    print(f'File Analyzed: {test_set_file}')
    print(f'Final Aim: {submarine_2.aim}')
    print(f'Y Pos: {submarine_2.pos_y}')
    print(f'Z Pos: {submarine_2.pos_z}')
