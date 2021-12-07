from aocd import data as day7_data
import time

start_time = time.perf_counter()

crabs = [int(s) for s in day7_data.strip().split(',')]
crab_min, crab_max, crab_len = min(crabs), max(crabs), len(crabs)

# Part One:
low_cost = (crab_max - crab_min) * crab_len
for dest in range(crab_min, crab_max+1):
    fuel_cost = []
    for source in crabs:
        fuel_cost.append(abs(source-dest))
    fuel_sum = sum(fuel_cost)
    if fuel_sum < low_cost:
        low_cost = fuel_sum
part1_answer = low_cost

# Part Two:
costs = {}
cost_calc = lambda source, dest, dist: (dist / 2 ) * (dist + 1)
low_cost = cost_calc(crab_min, crab_max, crab_max-crab_min) * crab_len
for dest in range(crab_min, crab_max+1):
    fuel_cost = []
    for source in crabs:
        dist = abs(dest-source)
        if dist in costs:
            fuel_cost.append(costs[dist])
            #print('match')
        else:
            my_cost = cost_calc(dest, source, dist)
            costs[dist] = my_cost
            fuel_cost.append(my_cost)
        #print(source, dest, dist, my_cost)
    fuel_sum = sum(fuel_cost)
    if fuel_sum < low_cost:
        low_cost = fuel_sum
part2_answer = int(low_cost)

end_time = time.perf_counter()

print(f"Part 1 answer: {part1_answer}")
print(f"Part 2 answer: {part2_answer}")
print(f"Seconds to calculate: {end_time - start_time:0.4f}")
