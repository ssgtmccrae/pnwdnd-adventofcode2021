from aocd import data as day5_data

ages = [int(x) for x in day5_data.strip().split(',')]

def fish(days, ages):
    days_to_run = days + 1
    birthdays = [0 for _ in range(days_to_run)]
    for age in ages:
        for i in range(age+1, len(birthdays), 7):
            birthdays[i] += 1

    for day, births in enumerate(birthdays):
        if day+9 < days_to_run:
            birthdays[day+9] += births
        for i in range(day+16, days_to_run, 7):
            birthdays[i] += births
    return sum(birthdays) + len(ages)

print(f"Part 1 total fish: {fish(80, ages)}")
print(f"Part 2 total fish: {fish(256, ages)}")
