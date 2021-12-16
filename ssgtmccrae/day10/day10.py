"""
Ryan McGregor, 15Dec2021
AOC2021:Day10
https://adventofcode.com/2021/day/10
"""

# from pprint import pprint
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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def bracket_check(file_contents):
    """
    Recursively checks if line brackets are correct, applying scores if not.
    Input: line
    Output: corruption_score (int), completion_scores (List[int]), corrected_lines (List[str])
    """
    corruption_score = 0
    completion_scores = []
    corrected_lines = []

    for line in file_contents:
        corrected_line = line
        changed = None
        while changed is not False:
            changed = False
            new_line = line
            new_line = new_line.replace('()','')
            new_line = new_line.replace('{}','')
            new_line = new_line.replace('[]','')
            new_line = new_line.replace('<>','')
            if new_line != line:
                changed = True
            line = new_line
        corruptors = [x for x in list(line) if x in [')','}',']','>']]
        if len(corruptors) > 0:
            corruption_score += SCORE_LEGEND[corruptors[0]]
            file_contents.remove(corrected_line)
        else:
            completion_score = 0
            line = list(line)
            line.reverse()
            for item in line:
                match item:
                    case '(':
                        corrected_line += ')'
                    case '{':
                        corrected_line += '}'
                    case '[':
                        corrected_line += ']'
                    case '<':
                        corrected_line += '>'
                completion_score = completion_score * 5 + SCORE_LEGEND[item]
            completion_scores.append(completion_score)
            corrected_lines.append(corrected_line)
    return corruption_score, sorted(completion_scores), corrected_line

if __name__ == '__main__':
    # print(bracket_check(test_set)) # Test Code
    dataset = get_data(year=2021, day=10).split('\n')
    bracket_stats = bracket_check(dataset)

    # Part 1
    print(f'Pt1 - Corruption Score: {bracket_stats[0]}')
    # Part 2
    middle_score = bracket_stats[1][len(bracket_stats[1])//2]
    print(f'Pt2 - Middle Completion Score: {middle_score}')
