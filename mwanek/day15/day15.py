import numpy as np
with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split('\n')
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
    visited = set()
    lowest_cost = {}
    to_visit.append(start_node)

    iterations = 0
    max_iterations = (len(risk_map) // 2) ** 6

    moves = [ (-1,  0),
              ( 1,  0),
              ( 0, -1),
              ( 0,  1)
            ]

    while to_visit:
        iterations += 1
        if iterations > max_iterations:
            raise RuntimeWarning(f"Too many iterations: {iterations}")

        current_node = to_visit[0]
        current_index = 0
        for index, node_to_visit in enumerate(to_visit):
            if node_to_visit.cost < current_node.cost:
                current_node = node_to_visit
                current_index = index

        to_visit.pop(current_index)
        visited.add(current_node.position)

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
            if child.position in visited:
                continue
            if [n for n in to_visit if child.position == n.position and child.cost >= n.cost]:
                continue
            to_visit.append(child)

def bigger_map(starting_map):
    row = []
    row.append(starting_map)
    for i in range(4):
        new_grid = row[i] + 1
        with np.nditer(new_grid, op_flags=['readwrite']) as it:
            for x in it:
                if x == 10:
                    x[...] = 1
        row.append(new_grid)
    columns = []
    columns.append(np.concatenate((row), axis=1))
    for i in range(4):
        new_grid = columns[i] + 1
        with np.nditer(new_grid, op_flags=['readwrite']) as it:
            for x in it:
                if x == 10:
                    x[...] = 1
        columns.append(new_grid)
    return np.concatenate(columns)

risk_map = []
for line in data:
    risk_map.append([int(char) for char in line])

risk_map = np.array(risk_map)
y_max, x_max = [i - 1 for i in np.shape(risk_map)]
start = (0, 0)
end = (y_max, x_max)

final_node = navigate(risk_map, start, end)

big_map = np.array(bigger_map(risk_map))
big_y_max, big_x_max = [i - 1 for i in np.shape(big_map)]
big_start = (0, 0)
big_end = (big_y_max, big_x_max)

final_big_node = navigate(big_map, big_start, big_end)

print("Part 1, final cost:", final_node.cost)
print("Part 2, final cost:", final_big_node.cost)
