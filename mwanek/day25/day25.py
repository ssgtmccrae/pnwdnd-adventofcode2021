from copy import copy, deepcopy
from typing import List
from collections import deque
from pprint import pprint

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split('\n')

test_data = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
""".strip().split('\n')
#data = test_data

EAST = 1
SOUTH = -1
EMPTY = 0

mapping = dict(zip(["v",".",">"], [SOUTH,EMPTY,EAST]))
rev_mapping = dict(zip([SOUTH,EMPTY,EAST], ["v",".",">"]))

def rotate_left(l) -> List[List[int]]:
    return list(reversed([list(x) for x in zip(*l)]))
def rotate_right(l) -> List[List[int]]:
    return [list(reversed(x)) for x in zip(*l)]

sea_floor = []

for line in data:
    sea_floor.append([mapping[char] for char in line])

def move(move_type, floor_state) -> List[List[int]]:
    new_floor = []
    for old_line in floor_state:
        new_line = copy(old_line)
        for i, cucumber in enumerate(old_line):
            if i+1 < len(old_line):
                if cucumber == move_type:
                    if not old_line[i+1]:
                        new_line[i] = 0
                        new_line[i+1] = move_type
            else:
                if cucumber == move_type:
                    if not old_line[0]:
                        new_line[i] = 0
                        new_line[0] = move_type
        new_floor.append(new_line)
    return new_floor

def step(floor_state) -> List[List[int]]:
    state_after_east_move = move(EAST, floor_state)
    floor_rotated_left = rotate_left(state_after_east_move)
    state_after_south_move = move(SOUTH, floor_rotated_left)
    return rotate_right(state_after_south_move)

for i in range(1, 5000):
    last = deepcopy(sea_floor)
    sea_floor = step(sea_floor)
    if last == sea_floor:
        print(f"No moves at step {i}")
        break
