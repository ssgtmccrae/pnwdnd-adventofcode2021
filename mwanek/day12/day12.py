from collections import defaultdict, namedtuple


with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split('\n')

test_data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""
data = test_data.strip().split('\n')

caves = defaultdict(list)
small_caves = []
big_caves = []
all_caves = []

for line in data:
    new_cave = line.split('-')
    caves[new_cave[0]].append(new_cave[1])
    caves[new_cave[1]].append(new_cave[0])
    all_caves.append(new_cave[0])
    all_caves.append(new_cave[1])
    if new_cave[0].isupper():
        big_caves.append(new_cave[0])
    else:
        small_caves.append(new_cave[0])
    if new_cave[1].isupper():
        big_caves.append(new_cave[1])
    else:
        small_caves.append(new_cave[1])

small_caves = set(small_caves)
big_caves = set(big_caves)
all_caves = list(set(all_caves))

#print(caves)
#print(big_caves)
#print(small_caves)
#print(all_caves)

my_paths = []

def find_all_paths(current, dest, visited, path):
    cave_id = all_caves.index(current)
    visited[cave_id] += 1
    path.append(current)

    if current == dest:
        my_paths.append(path)
    else:
        for neighbor in caves[current]:
            neighbor_id = all_caves.index(neighbor)
            if not visited[neighbor_id]:
                find_all_paths(neighbor, dest, visited, path)

    small_id = all_caves.index(path[-1])
    if visited[small_id] > 1 and path[-1] in small_caves:
        path.pop()
    path[cave_id] = 0

empty_path = []
to_visit = [0] * len(all_caves)

find_all_paths('start', 'end', to_visit, empty_path)
print(len(my_paths))
