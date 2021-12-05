"""
Ryan McGregor, 03Dec2021
AOC2021:Day04
https://adventofcode.com/2021/day/4
"""

import sys
import numpy as np
from pprint import pprint

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
        for _number in self.numbers:
            for _card in self.cards:
                for _card_line in _card:
                    if _number in _card.keys():
                        card_line[_number] = True
                        pprint(_card)

class BingoCard():
    """
    Manage a single Bingo Card.
    Maintains Numpy arrays for both the card and the callen numbers, then checks for a win.
    """
    card = None
    called_numbers = []

    def __init__(self, listed_card):
        self.card = np.array(listed_card, int)

    def check_win_status(self):
        card_mask = np.ones((len(self.card), len(self.card)))
        for number in self.called_numbers:
            pass

    def check_number(self, number):
        if number in self.card:
            loc = np.where(self.card == number)
            loc_list = []
            # [array([1,4]), array([2,2])]
            # array([1,4])
            for idx, coord in enumerate(loc[0].tolist()):
                loc_list.append((loc[0].tolist()[idx], loc[1].tolist()[idx]))
            return loc_list
        else:
            return None




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

    bingo = BingoGame(cards_clean, numbers_clean)
    pprint(bingo.cards[0].card)
    print(bingo.cards[0].check_number(101))
    print(bingo.cards[0].check_number(31))

    # pprint(bingo.numbers)
