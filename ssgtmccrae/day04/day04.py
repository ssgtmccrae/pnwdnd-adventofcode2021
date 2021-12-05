"""
Ryan McGregor, 03Dec2021
AOC2021:Day04
https://adventofcode.com/2021/day/4
"""

import sys
from pprint import pprint
import numpy as np
class BingoCard():
    """
    Manage a single Bingo Card.
    Maintains Numpy arrays for both the card and the callen numbers, then checks for a win.
    """
    card = None
    card_mask = None
    last_called = []
    numbers_called = 0
    winning_rowcol = None

    def __init__(self, listed_card):
        self.card = np.array(listed_card, int)
        self.card_mask = np.ones((len(self.card), len(self.card)))

    def check_winning_status(self):
        """
        Checks if a card has any completed rows or columns.
        Input: None
        Output: False (if non found) or str containing winning criteria
        """
        masked_card = self.card * self.card_mask
        dimensions = masked_card.shape[0]
        for idx in range(dimensions):
            # check_row
            if masked_card[idx, :].sum() == 0:
                self.winning_rowcol = f'row: {idx}'
            # check_column
            if masked_card[:, idx].sum() == 0:
                self.winning_rowcol = f'column: {idx}'

    def call_number(self, _number):
        """
        Modifies card mask with if number exists on card in one or more location.
        Input: _number (int)
        """
        if self.winning_rowcol is None:
            self.last_called = _number
            self.numbers_called += 1
            mask_item = self.check_card(int(_number))
            if mask_item is not None:
                for coord in mask_item:
                    self.card_mask[coord] = 0
            self.check_winning_status()

    def check_card(self, number):
        """
        Checks if a number exists in a card, and if so returns all coordinates it exists at.
        Input: number (int)
        Output: None (if doesn't exist), List[tuple(int,int)] containing coords if it does.
        """
        if number in self.card:
            loc = np.where(self.card == number)
            loc_list = []
            for idx in range(len(loc[0].tolist())):
                loc_list.append((loc[0].tolist()[idx], loc[1].tolist()[idx]))
            return loc_list
        return None


class BingoGame():
    """
    Handle bingo game, manage bingo cards. Cycles through bingo numbers, filling out cards and determining wins.
    Input: cards (List[List[Dict[int: bool]]]), numbers (List[int])
    """
    cards = []
    numbers = []

    def __init__(self, cards, numbers):
        self.numbers = numbers
        for _card in cards:
            self.cards.append(BingoCard(_card))
        self.numbers = numbers

    def run_game(self):
        """
        Run through bingo numbers, testing each card for win.
        Input: None
        Output: None
        """

        print(len(self.cards))

        for _number in self.numbers:
            print(f'Calling number: {_number}')
            for _card in self.cards:
                _card.call_number(_number)
        self.cards.sort(key= lambda x: x.numbers_called)
        print('Winning Cards Found:')
        for _card in self.cards:
            if _card.winning_rowcol is not None:
                print('Card:')
                pprint(_card.card)
                print('Unmarked Numbers:')
                unmarked_card = _card.card_mask * _card.card
                pprint(unmarked_card)
                print(f'Sum: {unmarked_card.sum()}')
                print(f'Winning Row/Col: {_card.winning_rowcol}')
                print(f'Last number called: {_card.last_called}')
                print(f'Numbers Called: {_card.numbers_called}')

if __name__ == '__main__':
    bingo_cards_file, bingo_numbers_file = sys.argv[1], sys.argv[2]
    # Clean data from bingo cards file
    with open(bingo_cards_file, 'r', encoding="utf-8") as file:
        card_list = file.read().split('\n')
    card = []
    cards_clean = []
    while len(card_list) > 0:
        card_line = card_list.pop(0).split()
        if card_line != []:
            # card_line_dict = {x: False for x in card_line}
            card.append(card_line)
            if len(card) == 5:
                cards_clean.append(card.copy())
                card = []
    # Clean data from bingo numbers file
    with open(bingo_numbers_file, 'r', encoding="utf-8") as file:
        number_list = file.read()
    numbers_clean = number_list.strip().split(',')
    bingo = BingoGame(cards_clean, numbers_clean)
    bingo.run_game()
