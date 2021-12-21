import re
from collections import defaultdict, namedtuple
from typing import Dict

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip()

class LoadedDice:
    def __init__(self) -> None:
        self.value = 0
    def roll(self):
        self.value += 1
        ret_val = self.value % 100
        return self.value % 100 if ret_val > 0 else 100

p1_pos, p2_pos = [int(i) for i in re.findall(r": (\d)", data)]
p1_score, p2_score = 0, 0
dice = LoadedDice()

rolls = 0
while True:
    rolls += 3
    p1_pos = (p1_pos + dice.roll() + dice.roll() + dice.roll()) % 10
    p1_score += p1_pos if p1_pos else 10
    if p1_score >= 1000:
        break
    rolls += 3
    p2_pos = (p2_pos + dice.roll() + dice.roll() + dice.roll()) % 10
    p2_score += p2_pos if p2_pos else 10
    if p2_score >= 1000:
        break

print("Part 1, best to 1k, loaded dice:", min([p1_score, p2_score]) * rolls)

p1_pos, p2_pos = [int(i) for i in re.findall(r": (\d)", data)]

BoardState = namedtuple("BoardState", "p1_pos p1_score p2_pos p2_score to_play")

ROLLS = []
for die1 in range(1,4):
    for die2 in range(1,4):
        for die3 in range(1,4):
            ROLLS.append(die1 + die2 + die3)

def roll_dice(universes: Dict[BoardState, int]):
    p1_wins = 0
    p2_wins = 0
    new_universes = defaultdict(int)

    for board, num_universes in universes.items():
        if board.to_play == 1:
            for roll in ROLLS:
                new_pos = board.p1_pos + roll
                if new_pos > 10:
                    new_pos -= 10
                new_score = board.p1_score + new_pos
                if new_score >= 21:
                    p1_wins += num_universes
                else:
                    new_board_state = BoardState(
                        p1_pos = new_pos,
                        p1_score = new_score,
                        p2_pos = board.p2_pos,
                        p2_score = board.p2_score,
                        to_play = 2
                    )
                    new_universes[new_board_state] += num_universes
        elif board.to_play == 2:
            for roll in ROLLS:
                new_pos = board.p2_pos + roll
                if new_pos > 10:
                    new_pos -= 10
                new_score = board.p2_score + new_pos
                if new_score >= 21:
                    p2_wins += num_universes
                else:
                    new_board_state = BoardState(
                        p1_pos = board.p1_pos,
                        p1_score = board.p1_score,
                        p2_pos = new_pos,
                        p2_score = new_score,
                        to_play = 1
                    )
                    new_universes[new_board_state] += num_universes

    return new_universes, p1_wins, p2_wins

universes = defaultdict(int)
game_start = BoardState(
    p1_pos = p1_pos,
    p2_pos = p2_pos,
    p1_score = 0,
    p2_score = 0,
    to_play = 1
)
universes[game_start] = 1

p1_total_wins = 0
p2_total_wins = 0

while universes:
    universes, p1_wins, p2_wins = roll_dice(universes)
    p1_total_wins += p1_wins
    p2_total_wins += p2_wins

print("Part 2, universal wins:", max([p1_total_wins, p2_total_wins]))
