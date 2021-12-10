from collections import namedtuple
import numpy as np
from collections import deque

with open("input.txt", "r") as file:
    data = file.read()

data = data.strip().split('\n')

Chars = namedtuple("Chars", "openers, closers, error_scores, comp_scores")
CHARS = Chars(
            openers=("(", "[", "{", "<"),
            closers=(")", "]", "}", ">"),
            error_scores=(3, 57, 1197, 25137),
            comp_scores=(1,2,3,4)
            )

def chunk_match(char: str) -> str:
    if char in CHARS.openers:
        return CHARS.closers[CHARS.openers.index(char)]
    elif char in CHARS.closers:
        return CHARS.openers[CHARS.closers.index(char)]
    else:
        raise ValueError

def error_score(char: str) -> int:
    if char in CHARS.closers:
        return CHARS.error_scores[CHARS.closers.index(char)]
    else:
        raise ValueError

def comp_score(char: str) -> int:
    if char in CHARS.openers:
        return CHARS.comp_scores[CHARS.openers.index(char)]
    else:
        raise ValueError

syntax_error_score = 0
comp_scores = []

for line in data:
    my_stack = deque()
    syntax_error = False
    for char in line:
        if char in CHARS.openers:
            my_stack.append(char)
        elif char in CHARS.closers:
            match_char = my_stack.pop()
            if match_char != chunk_match(char):
                syntax_error_score += error_score(char)
                syntax_error = True
                break
    if not syntax_error:
        my_comp_score = 0
        while len(my_stack) > 0:
            incomplete_char = my_stack.pop()
            my_comp_score *= 5
            my_comp_score += comp_score(incomplete_char)
        comp_scores.append(my_comp_score)

median_comp_score = int(np.median(comp_scores))

print(f"Part 1, syntax error score: {syntax_error_score}")
print(f"Part 2, median autocomplete score: {median_comp_score}")
