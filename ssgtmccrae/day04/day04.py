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
    Input: cards (List[List[List[int]]]), numbers (List[int])
    """
    def __init__(self, cards, numbers):
        self.numbers = numbers
        for card in cards:
            self.cards.append(np.array





# class BingoCard():

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
            card.append(card_line)
            if len(card) == 5:
                cards_clean.append(card.copy())
                card = []
    # Clean data from bingo numbers file
    with open(bingo_numbers_file, 'r', encoding="utf-8") as file:
        number_list = file.read()
    numbers_clean = number_list.strip().split(',')

"""     print('===========')
    print('number_list')
    print('===========')
    pprint(numbers_clean)

    print('===========')
    print('card_list')
    print('===========')
    pprint(cards_clean) """
