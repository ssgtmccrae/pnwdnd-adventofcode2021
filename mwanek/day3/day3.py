from aocd import lines as day3_input # pylint: disable=no-name-in-module
import math

def get_most_common_digit_for_every_index(list_of_numbers) -> str:
    ones_found = [ 0 for _ in range(12) ]
    for binary_number in list_of_numbers:
        for index, digit in enumerate(binary_number):
            if digit == "1":
                ones_found[index] += 1

    most_common = ""
    half_of_the_list = len(list_of_numbers) / 2
    for amount in ones_found:
        most_common += ("1" if amount >= half_of_the_list else "0")

    return most_common

def flip_ones_and_zeros(binary_number_as_string) -> str:
    new_number = ""
    for digit in binary_number_as_string:
        new_number += "1" if digit == "0" else "0"
    return new_number

def not_last_item(list_of_numbers) -> bool:
    return isinstance(list_of_numbers, list) and len(list_of_numbers) > 1

def filter_and_return(filter_by, list_of_numbers, index):
    new_list = []
    for binary_number in list_of_numbers:
        if not_last_item(list_of_numbers):
            if filter_by[index] == binary_number[index]:
                new_list.append(binary_number)
        else:
            break
    return new_list

def filter_until_one_remains(list_of_numbers, filter_by_most_common: bool) -> str:
    for index in range(12):
        if not_last_item(list_of_numbers):
            most_common = get_most_common_digit_for_every_index(list_of_numbers)
            if filter_by_most_common:
                list_of_numbers = filter_and_return(most_common, list_of_numbers, index)
            else:
                least_common = flip_ones_and_zeros(most_common)
                list_of_numbers = filter_and_return(least_common, list_of_numbers, index)
        else:
            break
    return list_of_numbers[0]

most_common_digits = get_most_common_digit_for_every_index(day3_input[:])
least_common_digits = flip_ones_and_zeros(most_common_digits)

final_number_filtered_by_most_common = filter_until_one_remains(
    day3_input[:], filter_by_most_common=True
)
final_number_filtered_by_least_common = filter_until_one_remains(
    day3_input[:], filter_by_most_common=False
)

str_to_decimal = lambda x: int(x, 2)
part1_answer = str_to_decimal(most_common_digits) * str_to_decimal(least_common_digits)
part2_components = [
    final_number_filtered_by_most_common,
    final_number_filtered_by_least_common
]
part2_components_in_decimal = list(map(str_to_decimal, part2_components))
part2_answer = math.prod(part2_components_in_decimal)

print("Part 1 answer:", part1_answer)
print("Part 2 answer:", part2_answer)
