from collections import defaultdict, Counter, deque
from dataclasses import dataclass

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split('\n')

@dataclass
class Node:
    name: str
    path: list

def number_of_paths(connections, limited_nodes, limit):
    start = "start"
    end = "end"
    start_node = Node(start, [start])
    end_node = Node(end, [end])

    to_visit = deque()
    to_visit.append(start_node)
    found_paths = 0

    while to_visit:
        current_node = to_visit.pop() # lol way faster than pop(0), thanks Andrew

        if current_node.name == end_node.name:
            found_paths += 1
            continue

        child_nodes = []

        for next_node in connections[current_node.name]:
            new_node = Node(next_node, current_node.path + [next_node])
            child_nodes.append(new_node)

        for child in child_nodes:
            if child.name == start:
                continue
            if child.name in limited_nodes:
                limits_reached = 0
                for node in limited_nodes:
                    node_count = child.path.count(node)
                    if node_count > 2:
                        limits_reached = limit + 1
                    if node_count > 1:
                        limits_reached += 1
                    if limits_reached > limit:
                        break
                if limits_reached > limit:
                    continue
            to_visit.append(child)

    return(found_paths)

caves = defaultdict(list)
small_caves = set()

for line in data:
    cave, next_cave = line.split('-')
    caves[cave].append(next_cave)
    caves[next_cave].append(cave)
    if cave.islower():
        small_caves.add(cave)
    if next_cave.islower():
        small_caves.add(next_cave)

print("Part 1, one visit per small cave:", number_of_paths(caves, small_caves, 0))
print("Part 2, same + two visits for one small cave:", number_of_paths(caves, small_caves, 1))
