import re
from itertools import product


def parse(line):
    action, *vertices = re.match(
        r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", line
    ).groups()
    return action, *map(int, vertices)


with open("data") as f:
    instructions = [parse(line) for line in f.read().splitlines()]

size = 1000

# ==== PART 1 ====
lights = [0] * size**2
for action, x, y, u, v in instructions:
    for t, s in product(range(x, u + 1), range(y, v + 1)):
        match action:
            case "turn on":
                lights[t + s * size] = 1
            case "turn off":
                lights[t + s * size] = 0
            case "toggle":
                lights[t + s * size] = 1 - lights[t + s * size]
print(sum(lights))


# ==== PART 2 ====
lights = [0] * size**2
actions = {"turn on": 1, "turn off": -1, "toggle": 2}
for action, x, y, u, v in instructions:
    for t, s in product(range(x, u + 1), range(y, v + 1)):
        lights[t + s * size] = max(0, lights[t + s * size] + actions[action])
print(sum(lights))
