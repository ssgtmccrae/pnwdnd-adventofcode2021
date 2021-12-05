"""
Ryan McGregor, 03Dec2021
AOC2021:Day04
https://adventofcode.com/2021/day/4
"""

import sys
import numpy as np
from pprint import pprint

from numpy.lib.index_tricks import CClass

class BingoCard():
    """
    Manage a single Bingo Card.
    Maintains Numpy arrays for both the card and the callen numbers, then checks for a win.
    """
    card = None
    card_mask = None

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
                return f'row: {idx}'
            # check_column
            if masked_card[:, idx].sum() == 0:
                return f'column: {idx}'
        return False

    def call_number(self, _number):
        """
        Modifies card mask with if number exists on card in one or more location.
        """
        mask_item = self.check_card(_number)
        if mask_item is not None:
            for coord in mask_item:
                self.card_mask[coord] = 0

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
        else:
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

        winning_cards = []
        current_numbers = self.numbers.copy()
        numbers_called = []

        while len(winning_cards) == 0 and len(current_numbers) > 0:
            _number = current_numbers.pop(0)
            numbers_called.append(_number)
            print(f'Calling number: {_number}')
            for _card in self.cards:
                _card.call_number(_number)
                pprint(_card.card_mask)
                if _card.check_winning_status() != False:
                    winning_cards.append(_card)
        if len(winning_cards) > 0:
            print('Winning Cards Found!')
            print(f'Numbers Called: {numbers_called}')
            for _card in winning_cards:
                pprint(_card.card)
        else:
            print('No winning cards found :-(')

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

    # print('===========')
    # print('number_list')
    # print('===========')
    # pprint(numbers_clean)

    # print('===========')
    # print('card_list')
    # print('===========')
    # pprint(cards_clean)

    # bingo = BingoGame(cards_clean, numbers_clean)
    bingo = BingoGame(cards_clean, numbers_clean)
    bingo.run_game()
    # pprint(bingo.cards[0].card)
    # pprint(bingo.cards[0].check_winning_status())
    # for x in [83,67,12,59,98,4]:
    #     bingo.cards[0].call_number(x)
    # pprint(bingo.cards[0].card_mask)
    # pprint(bingo.cards[0].check_winning_status())
    # for x in [83, 50, 75, 12,  36]:
    #     bingo.cards[0].call_number(x)
    # pprint(bingo.cards[0].check_winning_status())
    # pprint(bingo.cards[0].card_mask)


    # pprint(bingo.numbers)
