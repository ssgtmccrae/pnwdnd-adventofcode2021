from aocd import lines as day5_lines
from collections import namedtuple

raw_lines = [line.split('->') for line in day5_lines]

Point = namedtuple("Point", "x y")
VentLine = namedtuple("VentLine", "start end")

vent_lines = []
for line in raw_lines:
    coords = [list(map(int, xy.strip().split(','))) for xy in line]
    new_line = VentLine(
                Point(coords[0][0], coords[0][1]),
                Point(coords[1][0], coords[1][1])
            )
    vent_lines.append(new_line)

max_x = max([line.start.x for line in vent_lines] + [line.end.x for line in vent_lines])
max_y = max([line.start.y for line in vent_lines] + [line.end.y for line in vent_lines])

part1_graph = []
part2_graph = []
for _ in range(max_x+1):
    part1_graph.append([0 for _ in range(max_y+1)])
    part2_graph.append([0 for _ in range(max_y+1)])

horizontal_lines = [line for line in vent_lines if line.start.y == line.end.y]
vertical_lines = [line for line in vent_lines if line.start.x == line.end.x]

for line in horizontal_lines:
    left = min([line.start.x, line.end.x])
    right = max([line.start.x, line.end.x])+1
    for x in range(left, right):
        part1_graph[x][line.start.y] += 1
        part2_graph[x][line.start.y] += 1

for line in vertical_lines:
    bottom = min([line.start.y, line.end.y])
    top = max([line.start.y, line.end.y])+1
    for y in range(bottom, top):
        part1_graph[line.start.x][y] += 1
        part2_graph[line.start.x][y] += 1

for line in vent_lines:
    if line.start.x == line.end.x or line.start.y == line.end.y:
        continue
    left = line.start if line.start.x < line.end.x else line.end
    right = line.end if left == line.start else line.start
    x_dist = right.x - left.x
    y_dist = abs(right.y - left.y)
    if x_dist == y_dist:
        upwards = left.y < right.y
        downwards = not upwards
        if upwards:
            for step in range(x_dist+1):
                part2_graph[left.x+step][left.y+step] += 1
        if downwards:
            for step in range(x_dist+1):
                part2_graph[left.x+step][left.y-step] += 1

flattened_part1 = [item for sublist in part1_graph for item in sublist]
flattened_part2 = [item for sublist in part2_graph for item in sublist]
print("Part 1:", len([p for p in flattened_part1 if p > 1]))
print("Part 2:", len([p for p in flattened_part2 if p > 1]))
