from collections import defaultdict, Counter
from dataclasses import dataclass
from timeit import timeit

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

    to_visit = []
    to_visit.append(start_node)
    found_paths = 0

    while to_visit:
        current_node = to_visit[0]
        to_visit.pop(0)

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
                # 30% slower, but it "doesn't iterate" lol
                """
                is_limited = lambda node: node in limited_nodes
                limited_visits = list(filter(is_limited, child.path))
                limited_visit_counts = list(Counter(limited_visits).values())
                visited_twice = lambda count: count > 1
                visited_more_than_twice = lambda count: count > 2
                rule_1_violated = len(list(filter(visited_twice, limited_visit_counts))) > limit
                rule_2_violated = list(filter(visited_more_than_twice, limited_visit_counts))
                if rule_1_violated:
                    continue
                if rule_2_violated:
                    continue
                """
                # My original solution
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
                #"""
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

#print(timeit('number_of_paths(caves, small_caves, 0)', globals=globals(), number=5) / 5)
#print(timeit('number_of_paths(caves, small_caves, 1)', globals=globals(), number=5) / 5)

print("Part 1, one visit per small cave:", number_of_paths(caves, small_caves, 0))
print("Part 2, same + two visits for one small cave:", number_of_paths(caves, small_caves, 1))
