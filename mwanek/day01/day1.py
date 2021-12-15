import pathlib
path_to_input = pathlib.Path('input.txt')

with path_to_input.open('r') as file:
    day1_raw_input = file.read()

day1_input = [int(i) for i in day1_raw_input.split()]

def get_increases(list_to_count):
    increases = 0
    for index, value in enumerate(list_to_count):
        if index > 0:
            prev = index - 1
            if value > list_to_count[prev]:
                increases += 1
    return increases

def make_triplet_sums(list_to_sum):
    sums = []
    for index, value in enumerate(list_to_sum):
        if index + 3 <= len(list_to_sum):
            one = list_to_sum[index + 1]
            two = list_to_sum[index + 2]
            sums.append(value + one + two)
    return sums


part1_answer = get_increases(day1_input)
part2_answer = get_increases(make_triplet_sums(day1_input))

print("Part 1: Depth increases =", part1_answer)
print("Part 2: Measurement increases =", part2_answer)
