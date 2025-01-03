from copy import deepcopy
from itertools import product


def nn(x, y, Lx, Ly):
    return [
        (x + a, y + b)
        for (a, b) in set(product((-1, 0, 1), repeat=2)) - {(0, 0)}
        if 0 <= x + a < Lx and 0 <= y + b < Ly
    ]


def toggle(lights, neighbors, Lx, Ly, corners):
    toggled = deepcopy(lights)
    for x, y in product(range(Lx), range(Ly)):
        if corners and (x, y) in corners:
            continue
        neighbors_on = sum(lights[b][a] for a, b in neighbors[y][x])
        toggled[y][x] = neighbors_on in {2, 3} if lights[y][x] else (neighbors_on == 3)
    return toggled


def evolve(lights, neighbors, Lx, Ly, time, corners=None):
    for _ in range(time):
        lights = toggle(lights, neighbors, Lx, Ly, corners)
    return lights


with open("data") as f:
    start = [[x == "#" for x in l] for l in f.read().splitlines()]
Lx = len(start[0])
Ly = len(start)
neighbors = [[nn(x, y, Lx, Ly) for x in range(Lx)] for y in range(Ly)]

# ==== PART 1 ====
lights = evolve(deepcopy(start), neighbors, Lx, Ly, 100)
print(sum(sum(row) for row in lights))

# ==== PART 2 ====
corners = {(0, 0), (Lx - 1, 0), (0, Ly - 1), (Lx - 1, Ly - 1)}
for x, y in corners:
    start[y][x] = True
lights = evolve(start, neighbors, Lx, Ly, 100, corners)
print(sum(sum(row) for row in lights))
