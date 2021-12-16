"""
Ryan McGregor, 15Dec2021
AOC2021:Day09
https://adventofcode.com/2021/day/9
"""

from collections import namedtuple
from pprint import pprint
from aocd import get_data

TEST_SET_RAW = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''
test_set = TEST_SET_RAW.split('\n')

SCORE_LEGEND = {
    '(': 3,
    '[': 57,
    '{': 1197,
    '<': 25137,
}

def bracket_check(file_contents):
    """
    Recursively checks if line brackets are correct, applying scores if not.
    Input: line
    Output: score (int)
    """
    score = 0
    for line in file_contents:
        score += __bracket_check(list(line), score)
    return score

def __bracket_check(line, score):
    print(line)
    x = line.pop(0)
    if x in ['(','[','{','<']:
        try:
            match x:
                case '(':
                    y_idx = line.index(')')
                case '[':
                    y_idx = line.index(']')
                case '{':
                    y_idx = line.index('}')
                case '<':
                    y_idx = line.index('>')
            y = line.pop(y_idx)
            print(f'match for {x} found, line remaining: {line}' )
        except:
            print(f'match to {x} not found')
            score += SCORE_LEGEND[x]
    if len(line) > 0:
        score = __bracket_check(line, score)
    return score

if __name__ == '__main__':
    # topomap = TopoMap(test_set) # Test Code
    dataset = get_data(year=2021, day=10).split('\n')
    # pprint(dataset)
    print(bracket_check(test_set))
