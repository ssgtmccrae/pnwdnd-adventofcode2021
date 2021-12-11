"""
Advent of Code, 2021: Puzzle 10
"""
from collections import namedtuple
from collections import deque
import numpy as np

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split('\n')

Pair = namedtuple("Pair", "opener, closer")
PAIRS = [
        Pair("(", ")"),
        Pair("[", "]"),
        Pair("{", "}"),
        Pair("<", ">")
        ]
OPENERS = [pair.opener for pair in PAIRS]
CLOSERS = [pair.closer for pair in PAIRS]
OPENER_FOR = dict(zip(CLOSERS, OPENERS))
SYNTAX_ERROR_SCORE_FOR = dict(zip(CLOSERS, [3,57,1197,25137]))
COMPLETION_SCORE_FOR = dict(zip(OPENERS, [1,2,3,4]))

syntax_error_score = 0      #pylint: disable=invalid-name
completion_scores = []      #pylint: disable=invalid-name

for line in data:
    my_stack = deque()
    try:
        for character in line:
            if character in OPENERS:
                my_stack.append(character)
            elif character in CLOSERS:
                opener = my_stack.pop()
                if opener is not OPENER_FOR[character]:
                    raise SyntaxError
            else:
                raise KeyError
        my_completion_score = 0     #pylint: disable=invalid-name
        while len(my_stack) > 0:
            opener = my_stack.pop()
            my_completion_score *= 5
            my_completion_score += COMPLETION_SCORE_FOR[opener]
        completion_scores.append(my_completion_score)
    except SyntaxError:
        syntax_error_score += SYNTAX_ERROR_SCORE_FOR[character]

median_completion_score = round(np.median(completion_scores))

print(f"Part 1, syntax error score: {syntax_error_score}")
print(f"Part 2, median autocomplete score: {median_completion_score}")
