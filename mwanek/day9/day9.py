#from acod import data as day5_data

from collections import namedtuple
import numpy as np

with open("input.txt", "r") as file:
    data = file.read()#.strip().split('\n')


test_data = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""

rawmap = []
for line in data.strip().split():
    rawmap.append([int(p) for p in line])

x_max = len(rawmap[0])-1
y_max = len(rawmap)-1

lowpoints = []
edges = []
for y, row in enumerate(rawmap):
    for x, height in enumerate(row):
        if rawmap[y][x] == 9:
            edges.append((y, x))
        if x - 1 >= 0:
            left = rawmap[y][x-1]
        else: left = 10
        if x + 1 <= x_max:
            right = rawmap[y][x+1]
        else: right = 10
        if y - 1 >= 0:
            up = rawmap[y-1][x]
        else: up = 10
        if y + 1 <= y_max:
            down = rawmap[y+1][x]
        else: down = 10
        if height < left and height < right and height < down and height < up:
            lowpoints.append((y,x))

HeightMap = namedtuple("HeightMap", "map y_max x_max")

heightmap = HeightMap(rawmap, y_max, x_max)

def valid_adjacent_points(heightmap: HeightMap, point):
    y = point[0]
    x = point[1]
    points = []
    if x - 1 >= 0:
        if heightmap.map[y][x-1] != 9:
            points.append((y,x-1))
    if x + 1 <= heightmap.x_max:
        if heightmap.map[y][x+1] != 9:
            points.append((y,x+1))
    if y - 1 >= 0:
        if heightmap.map[y-1][x] != 9:
            points.append((y-1,x))
    if y + 1 <= heightmap.y_max:
        if heightmap.map[y+1][x] != 9:
            points.append((y+1,x))
    return points

def find_basin(heightmap: HeightMap, visited, point):
    my_basin = [point]
    for point_to_check in valid_adjacent_points(heightmap, point):
        if point_to_check not in visited:
            visited += my_basin
            visited += point_to_check
            my_basin += find_basin(heightmap, visited, point_to_check)
    return my_basin

basin_sizes = []
claimed = []
for point in lowpoints:
    my_basin = find_basin(heightmap, claimed, point)
    claimed += my_basin
    basin_sizes.append(len(set(my_basin))) # Why were there extra points? It's a mystery,

print(basin_sizes)

<<<<<<< HEAD
=======
print(basin_sizes)

>>>>>>> de468097d45e1f11c06e405ea6733a6f32ce02dd
print(sorted(basin_sizes, reverse=True)[0:3])
