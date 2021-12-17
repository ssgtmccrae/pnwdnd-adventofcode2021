from collections import namedtuple
import re

with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip()#.split('\n')

data = [int(i) for i in re.findall(r"x=(\d*)..(\d*), y=(-?\d*)..(-?\d*)", data).pop()]
Target = namedtuple("Target", "x_min x_max y_min y_max")
target = Target(*data)

def get_max_height(y_velocity):
    y = 0
    for i in range(1, y_velocity):
        y += i
    return y

def get_min_x_velocity(x_min, x_max):
    x = 0
    for i in range(1, x_min):
        x += i
        if x_min <= x <= x_max:
            return i

VelocityLimits = namedtuple("Velocities", "x_min x_max y_min y_max")
limits = VelocityLimits(
    x_min=get_min_x_velocity(target.x_min, target.x_max),
    x_max=target.x_max,
    y_min=target.y_min,
    y_max=abs(target.y_min)
)

def launch(vel: list, t: Target):
    x, y = [0, 0]
    x_vel, y_vel = vel
    while x <= t.x_max and y >= t.y_min:
        x += x_vel
        y += y_vel
        if t.x_min <= x <= t.x_max and t.y_min <= y <= t.y_max:
            return True
        y_vel -= 1
        if x_vel > 0:
            x_vel -= 1

max_height = get_max_height(limits.y_max)
hits = 0
for x in range(limits.x_min, limits.x_max+1):
    for y in range(limits.y_min, limits.y_max):
        hits += 1 if launch((x, y), target) else 0

print("Part 1, maximum height shot:", max_height)
print("Part 2, every initial velocity:", hits)
