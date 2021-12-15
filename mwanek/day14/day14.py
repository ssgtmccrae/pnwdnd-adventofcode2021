from collections import namedtuple
from pprint import pprint


with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split('\n')

test_data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
#data = test_data.strip().split('\n')

template = data[0]

pairs = {}
empty_pair_counts = {}
individual_chars = ""

for line in data[2:]:
    parts = line.split(' -> ')
    pairs[parts[0]] = {
        "name" : parts[0],
        "amount" : 0,
        "child_pairs" : [parts[0][0] + parts[1], parts[1]+parts[0][1]]
    }
    empty_pair_counts[parts[0]] = 0
    individual_chars += parts[0]

individual_chars = set(individual_chars)
char_counts = {char:0 for char in individual_chars}

#Define original pairs
for i, char in enumerate(template):
    if i != len(template) - 1:
        pair = char + template[i+1]
        pairs[pair]["amount"] += 1
char_counts[char] += 1

for i in range(40):
    added_pairs = empty_pair_counts.copy()
    # Make children
    for pair in pairs.values():
        for child in pair["child_pairs"]:
            added_pairs[child] += pair["amount"]
    # Add new additions to pairs
    for pair in pairs.values():
        pair["amount"] = added_pairs[pair["name"]]

for pair in pairs.values():
    char_counts[pair["name"][0]] += pair["amount"]

my_max = max([count for count in char_counts.values()])
my_min = min([count for count in char_counts.values()])

print(my_max - my_min)
