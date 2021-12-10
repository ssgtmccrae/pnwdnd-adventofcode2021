from collections import namedtuple
import numpy as np
from collections import deque

with open("input.txt", "r") as file:
    data = file.read().strip().split('\n')

Pair = namedtuple("Pair", "opener, closer")
pairs = [
        Pair("(", ")"),
        Pair("[", "]"),
        Pair("{", "}"),
        Pair("<", ">")
        ]

opening_chars = [pair.opener for pair in pairs]
closing_chars = [pair.closer for pair in pairs]
opener_for = dict(zip(closing_chars, opening_chars))
closer_for = dict(zip(opening_chars, closing_chars))
syntax_error_scores = dict(zip(closing_chars, [3,57,1197,25137]))
comp_scores = dict(zip(opening_chars, [1,2,3,4]))

syntax_error_total = 0
comp_score_totals = []

for line in data:
    my_stack = deque()
    syntax_error = False
    for char in line:
        if char in opening_chars:
            my_stack.append(char)
        elif char in closeing_chars:
            opener = my_stack.pop()
            if opener != opener_for[char]:
                syntax_error_total += syntax_error_scores[char]
                syntax_error = True
                break
    if not syntax_error:
        my_comp_score = 0
        while len(my_stack) > 0:
            incomplete_char = my_stack.pop()
            my_comp_score *= 5
            my_comp_score += comp_scores[incomplete_char]
        comp_score_totals.append(my_comp_score)

median_comp_score = int(np.median(comp_score_totals))

print(f"Part 1, syntax error score: {syntax_error_total}")
print(f"Part 2, median autocomplete score: {median_comp_score}")
