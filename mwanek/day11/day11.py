import numpy as np
from typing import List
import copy

from termcolor import colored

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split('\n')

test_data = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
#data = test_data.strip().split('\n')

class Octopus():
    def __init__(self, starting_energy: int) -> None:
        self._energy = starting_energy
        self._neighbors = []
        self._flashing = False

    def increase_energy(self) -> None:
        self._energy += 1
        if self._energy > 9:
            self.flash()

    def step(self) -> None:
        self.increase_energy()

    def flash(self) -> None:
        if not self._flashing:
            self._flashing = True
            for octopus in self._neighbors:
                octopus.increase_energy()

    @property
    def energy(self) -> int:
        return self._energy if self._energy < 10 else 0

    @property
    def flashing(self):
        return self._flashing

    @flashing.setter
    def flashing(self, flashing_state):
        if not flashing_state and self._energy > 9:
            self._energy = 0
        self._flashing = flashing_state


    @property
    def neighbors(self):
        return self._neighbors
    @neighbors.setter
    def neighbors(self, octopi) -> None:
        self._neighbors = octopi

class OctopusGrid:
    def __init__(self, starting_grid: list) -> None:
        self.grid = []
        x_max = len(starting_grid[0])-1
        y_max = len(starting_grid)-1
        for row in starting_grid:
            self.grid.append([Octopus(int(energy)) for energy in row])
        for y, row in enumerate(self.grid):
            for x, octopus in enumerate(row):
                neighbors = []
                if y != 0:
                    if x != 0:
                        neighbors.append(self.grid[y-1][x-1]) #TL
                    if x != x_max:
                        neighbors.append(self.grid[y-1][x+1]) #TR
                    neighbors.append(self.grid[y-1][x]) #TM
                if x != 0:
                    neighbors.append(self.grid[y][x-1]) #L
                if x != x_max:
                    neighbors.append(self.grid[y][x+1]) #R
                if y != y_max:
                    if x != 0:
                        neighbors.append(self.grid[y+1][x-1])#BL
                    if x != x_max:
                        neighbors.append(self.grid[y+1][x+1]) #BR
                    neighbors.append(self.grid[y+1][x]) #BM
                octopus.neighbors = neighbors
        self.all_octopi = [octopus for row in self.grid for octopus in row]
        self._flashes = 0
        self._all_flashing = False

    def step(self):
        for octopus in self.all_octopi:
            octopus.step()
        self._flashes += sum([octopus.flashing for octopus in self.all_octopi])
        self._snapshot = copy.deepcopy(self.grid)
        if sum([octopus.flashing for octopus in self.all_octopi]) == len(self.all_octopi):
            self._all_flashing = True
        for octopus in self.all_octopi:
            octopus.flashing = False

    def print(self):
        for row in self._snapshot:
            for octopus in row:
                if octopus.flashing:
                    print(colored(f"{octopus.energy}", color="grey", on_color="on_white", attrs=['bold']), end="")
                else:
                    print(octopus.energy, end="")
            print()

    @property
    def all_flashing(self):
        return self._all_flashing

    @property
    def flashes(self):
        return self._flashes

grid = OctopusGrid(data)

steps = 0
while not grid.all_flashing:
    grid.step()
    steps += 1
grid.print()
print(steps)
