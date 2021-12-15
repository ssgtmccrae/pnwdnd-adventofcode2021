from aocd import data as bingo_data
from typing import List
from dataclasses import dataclass
from termcolor import colored
import re
@dataclass
class BingoCoord:
    x: int
    y: int
    number: int
    marked = False

class BingoBoard:
    def __init__(self, board_data: list) -> None:
        self.coords = []
        for y, coord_numbers in enumerate(board_data):
            for x, number in enumerate(coord_numbers):
                self.coords.append(BingoCoord(x, y, number))
        self.total_marks = 0
        self.board_size = 5
        self.bingo = False
        self.final_mark = False

    def get_number(self, number: int) -> BingoCoord:
        matching_coord = [coord for coord in self.coords if coord.number == number]
        return matching_coord[0] if len(matching_coord) == 1 else False

    def get_row(self, y: int) -> List[BingoCoord]:
        coords = [coord for coord in self.coords if coord.y == y]
        return coords if len(coords) == self.board_size else False

    def get_column(self, x: int) -> List[BingoCoord]:
        coords = [coord for coord in self.coords if coord.x == x]
        return coords if len(coords) == self.board_size else False

    def get_coord(self, x: int, y: int) -> BingoCoord:
        matching_coord = [coord for coord in self.coords if coord.x == x and coord.y == y]
        return matching_coord[0] if len(matching_coord) == 1 else False

    def state(self) -> None:
        for y in range(self.board_size):
            print(end=" ")
            for coord in self.get_row(y):
                if coord.marked:
                    print(colored(f"{coord.number:>2}", on_color="on_green", attrs=['bold']), end=" ")
                else:
                    print(f"{coord.number:>2}", end=" ")
            print()

    @property
    def unmarked_sum(self) -> int:
        return sum([coord.number for coord in self.coords if not coord.marked])

    def mark(self, number: int) -> bool:
        if not self.bingo:
            coord = self.get_number(number)
            if coord:
                coord.marked = True
                self.total_marks += 1
                self.check_for_bingo(coord)
                return True
        return False

    def check_for_bingo(self, last_mark: BingoCoord) -> None:
        if self.total_marks >= self.board_size:
            if all([coord.marked for coord in self.get_row(last_mark.y)]):
                self.final_mark = last_mark.number
                self.bingo = True
            if all([coord.marked for coord in self.get_column(last_mark.x)]):
                self.final_mark = last_mark.number
                self.bingo = True

class BingoHall:
    def __init__(self, bingo_boards: list, numbers_to_call: list) -> None:
        # Create boards from data
        # Create numbers to call from data
        self.boards = [BingoBoard(board) for board in bingo_boards]
        self.finished_boards = []
        self.numbers_to_call = numbers_to_call

    def announce_number(self, number: int) -> None:
        for board in self.boards:
            board.mark(number)
            if board.bingo and board not in self.finished_boards:
                self.finished_boards.append(board)

    def run_bingo(self) -> None:
        for number in self.numbers_to_call:
            if len(self.boards) is not len(self.finished_boards):
                self.announce_number(number)
            else:
                break

    @property
    def winner(self) -> BingoBoard:
        return self.finished_boards[0]

    @property
    def last_winner(self) -> BingoBoard:
        return self.finished_boards[-1]

bingo_lines = bingo_data.split('\n')
bingo_numbers = [int(x) for x in bingo_lines[0].split(',')]

parse = re.compile("[-+]?\d+")
to_ints = lambda s: list(map(int, parse.findall(s)))
bingo_boards = []
for i in range(2, len(bingo_lines), 6):
    bingo_boards.append(list(map(to_ints, bingo_lines[i:i+5])))

bingo_hall = BingoHall(bingo_boards, bingo_numbers)
bingo_hall.run_bingo()
print("First winner's board:")
bingo_hall.winner.state()
print("First winner's score:", bingo_hall.winner.unmarked_sum * bingo_hall.winner.final_mark, "\n")
print("Final winner's board:")
bingo_hall.last_winner.state()
print("Final winner's score:", bingo_hall.last_winner.unmarked_sum * bingo_hall.last_winner.final_mark)
