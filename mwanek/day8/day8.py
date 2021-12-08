from aocd import data as day8_data
from collections import namedtuple
import copy
test_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

data = day8_data.strip().split('\n')

raw_signals = [s.split('|') for s in data]

SignalData = namedtuple("SignalData", "input output")

signals = []

for signal in raw_signals:
    signals.append(
        SignalData(
            signal[0].strip().split(),
            signal[1].strip().split()
        )
    )

#uniq_amt = [2, 3, 4, 7]
#check_uniq = lambda s: len(set(s)) in uniq_amt
#uniques = []
#for signal in signals:
#    uniques.append(len([ uniq for uniq in signal.output if check_uniq(uniq) ]))
#print(sum(uniques))

output_sums = []
for signal in signals:
    digits = ["" for _ in range(10)]
    digits[1] = [s for s in signal.input if len(s) == 2].pop()
    digits[4] = [s for s in signal.input if len(s) == 4].pop()
    digits[7] = [s for s in signal.input if len(s) == 3].pop()
    digits[8] = [s for s in signal.input if len(s) == 7].pop()
    rights = digits[1]
    for string in signal.input:
        if all(char in string for char in rights) and len(string) == 5:
            digits[3] = string
    lefts = copy.copy(digits[8])
    for char in list(digits[3]):
        lefts = lefts.replace(char, '')
    for string in signal.input:
        if len(string) == 6:
            if all(char in string for char in lefts):
                if sum([char in string for char in rights]) == 1:
                    digits[6] = string
    for string in signal.input:
        if len(string) == 6:
            if all(char in string for char in lefts):
                if all([char in string for char in rights]):
                    digits[0] = string
    for string in signal.input:
        if len(string) == 6 and string != digits[0] and string != digits[6]:
            digits[9] = string
    topleft = copy.copy(digits[4])
    for char in list(digits[3]):
        topleft = topleft.replace(char, '')
    bottomleft = lefts.replace(topleft, '')
    for string in signal.input:
        if len(string) == 5 and string != digits[3]:
            if topleft in string and not bottomleft in string:
                digits[5] = string
            else:
                digits[2] = string

    digits = [''.join(sorted(list(digit))) for digit in digits]
    outputs = [''.join(sorted(list(digit))) for digit in signal.output]
    my_output = ""
    for output in outputs:
        my_output += str(digits.index(output))
    output_sums.append(int(my_output))
print(sum(output_sums))
