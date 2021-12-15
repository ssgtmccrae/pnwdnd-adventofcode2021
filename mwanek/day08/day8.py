from collections import namedtuple

with open("input.txt", "r") as file:
    data = file.read().strip().split('\n')

raw_signals = [s.split('|') for s in data]

SignalData = namedtuple("SignalData", "input output")

signals = []

for signal in raw_signals:
    signals.append(
        SignalData(
            sorted([set(s) for s in signal[0].strip().split()], key=len),
            [set(s) for s in signal[1].strip().split()]
        )
    )

output_totals = []
for signal in signals:
    digits = [None for _ in range(10)]
    digits[1] = signal.input[0]
    digits[4] = signal.input[2]
    digits[7] = signal.input[1]
    digits[8] = signal.input[9]
    # Solve for 9, 0, 6
    if digits[4].issubset(signal.input[6]):
        digits[9] = signal.input[6]
        if digits[7].issubset(signal.input[7]):
            digits[0] = signal.input[7]
            digits[6] = signal.input[8]
        else:
            digits[0] = signal.input[8]
            digits[6] = signal.input[7]
    elif digits[4].issubset(signal.input[7]):
        digits[9] = signal.input[7]
        if digits[7].issubset(signal.input[6]):
            digits[0] = signal.input[6]
            digits[6] = signal.input[8]
        else:
            digits[0] = signal.input[8]
            digits[6] = signal.input[6]
    else:
        digits[9] = signal.input[8]
        if digits[7].issubset(signal.input[7]):
            digits[0] = signal.input[7]
            digits[6] = signal.input[6]
        else:
            digits[0] = signal.input[6]
            digits[6] = signal.input[7]
    # Solve for 3, 5, 2
    if digits[1].issubset(signal.input[3]):
        digits[3] = signal.input[3]
        if len(digits[4] & signal.input[4]) == 3:
            digits[5] = signal.input[4]
            digits[2] = signal.input[5]
        else:
            digits[5] = signal.input[5]
            digits[2] = signal.input[4]
    elif digits[1].issubset(signal.input[4]):
        digits[3] = signal.input[4]
        if len(digits[4] & signal.input[3]) == 3:
            digits[5] = signal.input[3]
            digits[2] = signal.input[5]
        else:
            digits[5] = signal.input[5]
            digits[2] = signal.input[3]
    else:
        digits[3] = signal.input[5]
        if len(digits[4] & signal.input[4]) == 3:
            digits[5] = signal.input[4]
            digits[2] = signal.input[3]
        else:
            digits[5] = signal.input[3]
            digits[2] = signal.input[4]
    output_total = 0
    for i in range(10):
        if digits[i] == signal.output[0]:
            output_total += i * 1000
        if digits[i] == signal.output[1]:
            output_total += i * 100
        if digits[i] == signal.output[2]:
            output_total += i * 10
        if digits[i] == signal.output[3]:
            output_total += i
    output_totals.append(output_total)
print(sum(output_totals))

# Old part1:
#uniq_amt = [2, 3, 4, 7]
#check_uniq = lambda s: len(set(s)) in uniq_amt
#uniques = []
#for signal in signals:
#    uniques.append(len([ uniq for uniq in signal.output if check_uniq(uniq) ]))
#print(sum(uniques))
