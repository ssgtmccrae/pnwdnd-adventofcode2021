from aocd import data as day4_input # pylint: disable=no-name-in-module
import math
import itertools as it
import re
from dataclasses import dataclass
from termcolor import colored

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


@dataclass
class BingoCoord:
    value: int
    marked = False
    def __eq__(self, other):
        return self.value == other

class BingoBoard:
    def __init__(self, coords) -> None:
        # take the 5 lines and put them into coords
        # convert them to 5 lists of 5
        # list LOOP_NUMBER, INDEX ()
        # (0, 0) : BingoCoord(22) -> (4, 0) : BingoCoord(00)
        # (0, 4) : BingoCoord(01) -> (4, 4) : BingoCoord(19)
        lines = [l for l in coords.split("\n") if l]
        self.board = {}
        for row, values in enumerate(lines):
            for column, value in enumerate(values.split()):
                self.board[row, column] = BingoCoord(int(value))
        self.total_marked = 0 # Don't check for bingos unless 5

    def mark_value(self, number_to_mark):
        my_coord = [ coord for coord, value in self.board.items() if number_to_mark == value ]
        if my_coord:
            my_coord = my_coord[0]
            self.total_marked += 1
            self.board[my_coord].marked = True
            #print(f"I marked {number_to_mark} on this board: ")
            #self.print_board()
            #input()
            return True
        return False

    def find_bingo(self):
        if self.total_marked >= 5:
            for i in range(5):
                if all([value.marked for coord, value in self.board.items() if coord[0] == i]):
                    #print(f"Horizontal Bingo! Sum: {str(self.board_sum)}")
                    return True
                elif all([value.marked for coord, value in self.board.items() if coord[1] == i]):
                    #print(f"Vertical Bingo! Sum: {str(self.board_sum)}")
                    return True
        return False


    def print_board(self):
        print()
        for i in range(5):
            print()
            for j in range(5):
                if self.board[i, j].marked:
                    print(colored("{:>2}".format(str(self.board[i, j].value)), on_color="on_green", attrs=['bold']), end=" ")
                else:
                    print("{:2}".format(str(self.board[i,j].value)), end=" ")
        print()

    @property
    def board_sum(self):
        return sum([value.value for value in self.board.values() if not value.marked])

split_input = day4_input.split('\n\n')
numbers_to_call = split_input.pop(0).strip().split(',')
boards = split_input

#board_regex = re.compile(r"((?:(?:[ \d]{1,2} {0,2}){5}\n){5})")
#boards = re.findall(board_regex, day4_input)

#numbers_to_call_regex = re.compile(r"(?:\d{1,2},)+\d{1,2}\n")
#numbers_to_call = re.match(numbers_to_call_regex, day4_input).group(0).strip().split(',')

bingo_boards = [BingoBoard(board) for board in boards]

#for board in bingo_boards:
#    board.mark_value(16)
#    print([value.marked for coord, value in board.board.items() if value == 16])

for num in numbers_to_call:
    if not bingo_boards:
        break
    #print(f"Calling: {num}")
    for board in bingo_boards[:]:
        marked = board.mark_value(int(num))
        if marked:
            if board.find_bingo():
                bingo_boards.remove(board)
                #print("Board sum:", int(num) * board.board_sum)
            if not bingo_boards:
                print("Last sum:", int(num) * board.board_sum)
                break
        marked = False
