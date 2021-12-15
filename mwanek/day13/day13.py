import re
import numpy as np

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read()

coords = [(int(c[0]), int(c[1])) for c in re.findall(r"(\d+),(\d+)", data)]
folds = [(c[0], int(c[1])) for c in re.findall(r"fold along (\w)=(\d+)", data)]
x_max = max([coord[0] for coord in coords]) + 1
y_max = max([coord[1] for coord in coords]) + 1

array = np.array(coords)

paper = np.zeros((y_max,x_max), dtype=bool)
paper[array[:,1], array[:,0]] = True

def fold_it(my_paper, my_fold):
    if my_fold[0] == "y":
        top = my_paper[ :my_fold[1] ]
        bottom = my_paper[my_fold[1]+1:]
        bottom = np.flipud(bottom)
        height_diff = len(top) - len(bottom)
        if height_diff:
            my_extra = np.zeros((height_diff, len(top[0])), dtype=bool)
            bottom = np.concatenate((my_extra, bottom))
        return top+bottom

    if my_fold[0] == "x":
        left = my_paper[:, :my_fold[1] ]
        right = my_paper[:, my_fold[1]+1:]
        right = np.fliplr(right)
        return left+right

visible_dots = []
for fold in folds:
    paper = fold_it(np.copy(paper), fold)
    visible_dots.append(sum(sum(paper)))

print(f"Part 1, visible dots: {visible_dots[0]}")
print("Part 2:")
for line in paper:
    for char in line:
        if char:
            print("#", end="")
        else:
            print(" ", end="")
    print()
