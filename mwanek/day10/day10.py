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

openers = [pair.opener for pair in pairs]
closers = [pair.closer for pair in pairs]
opener_for = dict(zip(closers, openers))
closer_for = dict(zip(openers, closers))
syntax_error_score_for = dict(zip(closers, [3,57,1197,25137]))
completion_score_for = dict(zip(openers, [1,2,3,4]))

syntax_error_total = 0
completion_scores = []

for line in data:
    my_stack = deque()
    syntax_error = False
    for character in line:
        if character in openers:
            my_stack.append(character)
        elif character in closers:
            opener = my_stack.pop()
            if opener is not opener_for[character]:
                syntax_error_total += syntax_error_score_for[character]
                syntax_error = True
                break
        else:
            raise KeyError
    if not syntax_error:
        my_completion_score = 0
        while len(my_stack) > 0:
            opener = my_stack.pop()
            my_completion_score *= 5
            my_completion_score += completion_score_for[opener]
        completion_scores.append(my_completion_score)

median_completion_score = round(np.median(completion_scores))

print(f"Part 1, syntax error score: {syntax_error_total}")
print(f"Part 2, median autocomplete score: {median_completion_score}")
