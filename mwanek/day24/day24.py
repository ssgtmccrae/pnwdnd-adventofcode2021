"""
This "runs" the MONAD things but is barking up the wrong tree. I solved it by hand
by examining the input.
"""

from collections import deque,defaultdict
from copy import copy

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split('\n')

test_data = """inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
""".split('\n')
#data = test_data

def value(to_check: str, variables: dict):
    if to_check.isalpha():
        #print(to_check, variables)
        return variables[to_check]
    else:
        return int(to_check)

def run_monad(my_input: deque, my_program) -> int:
    vars = defaultdict(lambda: 0)
    for line in my_program:
        instruction, parameters = line.split(" ", 1)
        p = parameters.split(" ")
        match instruction:
            case "inp":
                vars[p[0]] = int(my_input.popleft())
            case "add":
                vars[p[0]] += value(p[1], vars)
            case "mul":
                vars[p[0]] *= value(p[1], vars)
            case "div":
                vars[p[0]] //= value(p[1], vars)
            case "mod":
                vars[p[0]] %= value(p[1], vars)
            case "eql":
                vars[p[0]] = 1 if vars[p[0]] == value(p[1], vars) else 0
    return vars["z"]

def sig_rev(length):
    for i in range(7, 0, -1):
        if length == 1:
            yield str(i)
        else:
            for x in sig_rev(length-1):
                yield str(i) + x

test = deque("1" * 14)

print(run_monad(test, data))
