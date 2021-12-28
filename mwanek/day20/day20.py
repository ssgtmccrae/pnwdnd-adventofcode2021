import numpy as np

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split('\n')

ALGO = [c for c in data[0]]
for i, c in enumerate(ALGO):
    ALGO[i] = 1 if c == "#" else 0

image = []
for line in data[2:]:
    new_line = []
    for c in line:
        new_line.append(1 if c == "#" else 0)
    image.append(new_line)
original = np.array(image)

def enhance(my_image, iteration):
    new_image = np.zeros(np.shape(np.pad(my_image,pad_width=1)), dtype=int)
    if iteration % 2:
        ref_image = np.pad(image, pad_width=2, mode='constant', constant_values=1)
    else:
        ref_image = np.pad(image, pad_width=2, mode='constant', constant_values=0)

    for index, _ in np.ndenumerate(new_image):
        ref_y, ref_x = index
        ref_string = []
        ref_string += list(ref_image[ref_y][ref_x:ref_x+3])
        ref_string += list(ref_image[ref_y+1][ref_x:ref_x+3])
        ref_string += list(ref_image[ref_y+2][ref_x:ref_x+3])
        ref_string = "".join([str(c) for c in ref_string])
        ref_index = int(ref_string, 2)
        new_image[ref_y][ref_x] = ALGO[ref_index]

    return new_image

image = np.copy(original)
for i in range(2):
    image = enhance(np.copy(image), i)
print("Part 1, lit pixels after 2 iterations:", sum(sum(image)))

image = np.copy(original)
for i in range(50):
    image = enhance(np.copy(image), i)
print("Part 2, lit pixels after 50 iterations:", sum(sum(image)))
