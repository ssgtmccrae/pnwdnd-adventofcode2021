import re
from collections import deque

with open("scanners.txt", "r", encoding="utf-8") as file:
    data = file.read().strip()


coords = deque(re.findall(r"x=(-?\d*), y=(-?\d*), z=(-?\d*)", data))

distances = []
while coords:
    to_check = coords.pop()
    for coord in coords:
        dist = abs(int(to_check[0]) - int(coord[0])) + abs(int(to_check[1]) - int(coord[1])) + abs(int(to_check[2]) - int(coord[2]))
        distances.append(dist)

print(max(distances))
