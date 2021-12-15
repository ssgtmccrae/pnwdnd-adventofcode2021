import numpy as np
import time
with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split('\n')

test_data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""
#data = test_data.strip().split('\n')

start_time = time.perf_counter()

class Node:
    def __init__(self, parent=None, position=None) -> None:
        self.parent = parent
        self.position = position
        self.cost = 0
    def __eq__(self, other):
        return self.position == other.position

def navigate(risk_map, start, end):
    start_node = Node(None, tuple(start))
    end_node = Node(None, tuple(end))
    y_max, x_max = [i - 1 for i in np.shape(risk_map)]

    to_visit = []
    visited = []
    to_visit.append(start_node)

    iterations = 0
    max_iterations = (len(risk_map) // 2) ** 7

    moves = [ (-1,  0),
              ( 1,  0),
              ( 0, -1),
              ( 0,  1)
            ]

    while to_visit:
        iterations += 1
        if iterations > max_iterations:
            print(f"Too many iterations: {iterations}")
            return False

        current_node = to_visit[0]
        current_index = 0
        for index, node_to_visit in enumerate(to_visit):
            if node_to_visit.cost < current_node.cost:
                current_node = node_to_visit
                current_index = index

        to_visit.pop(current_index)
        visited.append(current_node)

        if current_node == end_node:
            return current_node

        child_nodes = []

        for new_position in moves:
            node_position = ( current_node.position[0] + new_position[0],
                              current_node.position[1] + new_position[1]
            )
            if ( node_position[0] < 0 or
                 node_position[0] > y_max or
                 node_position[1] < 0 or
                 node_position[1] > x_max):
                continue
            new_node = Node(current_node, node_position)
            new_node.cost += current_node.cost + risk_map[node_position[0]][node_position[1]]
            child_nodes.append(new_node)

        for child in child_nodes:
            if [n for n in visited if child.position == n.position]:
                continue
            if [n for n in to_visit if child.position == n.position and child.cost >= n.cost]:
                continue
            to_visit.append(child)

        #print("Current:", current_node.position, current_node.cost)
        #print("Visited:", [(node.position, node.cost) for node in visited])
        #print("Queue:", [(node.position, node.cost) for node in to_visit])
        #input()

risk_map = []
for line in data:
    risk_map.append([int(char) for char in line])
y_max, x_max = [i - 1 for i in np.shape(risk_map)]

start = (0, 0)
end = (y_max, x_max)

final_node = navigate(risk_map, start, end)

print(final_node.cost)
print(time.perf_counter() - start_time)
