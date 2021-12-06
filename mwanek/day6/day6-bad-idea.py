from aocd import data as day5_data

test_data = """3,4,3,1,2"""

ages = [int(x) for x in day5_data.split(',')]

class LanternFish:
    def __init__(self, fish_age = None) -> None:
        default_age = 8
        self.age = fish_age if fish_age else default_age
        self._give_birth = False

    def get_older(self, days):
        if self.age > 0:
            self.age -= days
        else:
            self._give_birth = True

    @property
    def give_birth(self):
        if self._give_birth:
            self._give_birth = False
            self.age = 6
            return True
        else:
            return False

class FishSchool:
    def __init__(self, initial_fish_ages: list) -> None:
        self.school = [LanternFish(age) for age in initial_fish_ages]

    def simulate_day(self):
        new_fish = 0
        for fish in self.school[:]:
            fish.get_older(1)
            if fish.give_birth:
                new_fish +=1
        for _ in range(new_fish):
            self.school.append(LanternFish())

    @property
    def school_ages(self):
        return [fish.age for fish in self.school]
    @property
    def school_size(self):
        return len(self.school)

simulation_length_in_days = 256
lanternfish_school = FishSchool(ages)

for _ in range(simulation_length_in_days):
    lanternfish_school.simulate_day()

print(lanternfish_school.school_size)
