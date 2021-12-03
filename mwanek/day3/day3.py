from aocd import data, lines, numbers
import copy

def get_most_common (list_of_numbers):
    count = [ 0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0
    ]
    for line in list_of_numbers:
        for index, character in enumerate(line):
            if character == "1":
                count[index] += 1
    gamma = ""
    for value in count:
        gamma += ("1" if value >= len(list_of_numbers) / 2 else "0")
    return gamma

def get_least_common (list_of_numbers):
    count = [ 0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0
    ]
    for line in list_of_numbers:
        for index, character in enumerate(line):
            if character == "1":
                count[index] += 1
    epsilon = ""
    for value in count:
        epsilon += ("0" if value >= len(list_of_numbers) / 2 else "1")
    return epsilon

gamma = get_most_common(lines)
epsilon = get_least_common(lines)

print(int(gamma, 2) * int(epsilon, 2))

oxygen = copy.copy(lines)
co2 = copy.copy(lines)

def filter_and_return(filter, my_list, i):
    new_list = []
    for index, binary_number in enumerate(my_list):
        if not type(my_list) is str and len(my_list) > 1:
            if filter[i] == binary_number[i]:
                new_list.append(binary_number)
        else:
            break
    return new_list

for i in range(12):
    if not type(oxygen) is str and len(oxygen) > 1:
        most_common = get_most_common(oxygen)
        oxygen = filter_and_return(most_common, oxygen, i)
    else:
        break

for i in range(12):
    if not type(co2) is str and len(co2) > 1:
        least_common = get_least_common(co2)
        co2 = filter_and_return(least_common, co2, i)
    else:
        break

print(int(oxygen[0], 2) * int(co2[0], 2))
