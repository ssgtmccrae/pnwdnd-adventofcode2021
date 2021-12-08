"""
Ryan McGregor, 06Dec2021
AOC2021:Day07
https://adventofcode.com/2021/day/7
"""

import sys

def find_fuel_cost(point_list, test_num):
    """
    Find fuel cost of all points in point_list to test_num.
    Computing for Pt1 of Day07 Challenge.
    Input: point_list (List[int]), test_num (int)
    Output: int, total fuel cost
    """
    total_cost = 0
    for point in point_list:
        total_cost += abs(point - test_num)
    return total_cost

def find_cheapest_fuel_cost(point_list, test_num, test_num_cost):
    """
    Recursively finds if test_num is the cheapest meeting point.
    Input: point_list (List[int]), test_num (int)
    Output: int, cheapest meeting point
    """
    lower_point = test_num - 1
    upper_point = test_num + 1
    lower_cost = find_fuel_cost(point_list, lower_point)
    upper_cost = find_fuel_cost(point_list, upper_point)
    if lower_cost < test_num_cost:
        return find_cheapest_fuel_cost(point_list, lower_point, lower_cost)
    if upper_cost < test_num_cost:
        return find_cheapest_fuel_cost(point_list, upper_point, upper_cost)
    return test_num, test_num_cost

def find_meeting_point(point_list):
    """
    Finds the average of a sorted list then tests above or below that to find lower
    fuel requirements.
    Input: point_list (List([int])
    Output: None
    """
    list_avg = sum(point_list) / len(point_list)
    return find_cheapest_fuel_cost(point_list, list_avg, find_fuel_cost(point_list, list_avg))


if __name__ == '__main__':
    dataset = []
    data_file = sys.argv[1]
    with open(data_file, 'r', encoding="utf-8") as file:
        for line in file.read().split('\n'):
            if line != '':
                for num in line.split(','):
                    dataset.append(int(num))

    # dataset = [16,1,2,0,4,2,7,1,2,14] # Uses 37 Fuel w/ an meeting point of 2
    print(find_meeting_point(dataset))
