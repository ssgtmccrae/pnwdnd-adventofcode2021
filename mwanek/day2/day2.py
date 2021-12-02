import pathlib
path_to_input = pathlib.Path('day2_input.txt')

with path_to_input.open('r') as file:
    day2_raw_input = file.readlines()

day2_input = [s.rstrip() for s in day2_raw_input]
day2_input = ([s.split() for s in day2_input])

horizontal = sum([int(move[1]) for move in day2_input if "forward" in move[0]])
down = sum([int(move[1]) for move in day2_input if "down" in move[0]])
up = sum([int(move[1]) for move in day2_input if "up" in move[0]])
vertical = down - up


print ("Part 1: Calculated distance =", horizontal * vertical)

aim = 0
depth = 0
horizontal = 0
for move in day2_input:
    direction = move[0]
    distance = int(move[1])
    match direction:
        case "forward":
            horizontal += distance
            depth += distance * aim
        case "down":
            aim += distance
        case "up":
            aim -= distance

print("Part 2: Calculated distance =", horizontal * depth)
