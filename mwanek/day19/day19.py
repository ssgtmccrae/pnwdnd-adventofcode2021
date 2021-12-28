from collections import namedtuple,defaultdict, deque
import re
from pprint import pprint


with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split('\n\n')
with open("test.txt", "r", encoding="utf-8") as file:
    test_data = file.read().strip().split('\n\n')
#data = test_data

Coord = namedtuple("Coord", "x, y, z")

rotated = lambda x, y, z: [
    Coord(x, y, z),
    Coord(x, -z, y),
    Coord(x, -y, -z),
    Coord(x, z, -y),

    Coord(-y, x, z),
    Coord(z, x, y),
    Coord(y, x, -z),
    Coord(-z, x, -y),

    Coord(-x, -y, z),
    Coord(-x, -z, -y),
    Coord(-x, y, -z),
    Coord(-x, z, y),

    Coord(y, -x, z),
    Coord(z, -x, -y),
    Coord(-y, -x, -z),
    Coord(-z, -x, y),

    Coord(-z, y, x),
    Coord(y, z, x),
    Coord(z, -y, x),
    Coord(-y, -z, x),

    Coord(-z, -y, -x),
    Coord(-y, z, -x),
    Coord(z, y, -x),
    Coord(y, -z, -x),

]

unk_scanners = deque()

for lines in data:
    rotations = defaultdict(list)
    for scanner, (x,y,z) in enumerate(re.findall(r"(?:(-?\d{1,3}),(-?\d{1,3}),(-?\d{1,3}))", lines)):
        for rot, coord in enumerate(rotated(int(x), int(y), int(z))):
            rotations[rot].append(coord)
    for key, value in rotations.items():
        rotations[key] = set(value)
    unk_scanners.append(rotations)

#scanner0 = unk_scanners.popleft()[0]
#found_scanners = { Coord(0,0,0) : unk_scanners.popleft()[0] }
found_scanners = [unk_scanners.popleft()[0]]


#pprint(len(unk_scanners))
#input()

# known scanner = set of coords, scanner_to_search is all 24 rotations
def find_overlap(known_scanner, scanner_to_search):
    for beacon in known_scanner:
        for rotation in scanner_to_search.values():
            for coord in rotation:
                transform = tuple(map(lambda i, j: i - j, beacon, coord))
                new_coords = set([Coord(*map(lambda i, j: i + j, transform, xyz)) for xyz in rotation])
                if len(new_coords & known_scanner) >= 12:
                    return Coord(*transform), new_coords
    return False

#pprint(find_overlap(found_scanners[Coord(0,0,0)], unk_scanners[0]))
#pprint(find_overlap(unk_scanners[0][0], unk_scanners[3]))

#quit()

iterations = 0
while unk_scanners:
    iterations += 1
    print(f"Iteration #{iterations}")
    for known_beacons in list(reversed(found_scanners)):
        for unk_scanner in unk_scanners:
            result = find_overlap(known_beacons, unk_scanner)
            if result:
                print(f"{unk_scanners.index(unk_scanner)} > at {result[0]}")
                #pprint(result[1])
                unk_scanners.remove(unk_scanner)
                found_scanners.append(result[1])
                break
        if result: break

#iterations = 0
#while unk_scanners:
#    iterations += 1
#    print(f"Iteration #{iterations}")
#    for known_id, known_beacons in found_scanners.items():
#        for unk_scanner in unk_scanners:
#            result = find_overlap(known_beacons, unk_scanner)
#            if result:
#                print(f"{unk_scanners.index(unk_scanner)} > {known_id} at {result[0]}")
#                #pprint(result[1])
#                unk_scanners.remove(unk_scanner)
#                found_scanners[result[0]] = result[1]
#                break
#        if result: break

whole_set = set()
for beacons in found_scanners:
    whole_set = whole_set | beacons
pprint(len(whole_set))
