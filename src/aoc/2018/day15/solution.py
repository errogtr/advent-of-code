from collections import deque
from copy import deepcopy
from itertools import count, product
import click
from aoc.utils import read_data, timer


def parse(data):
    units = [dict(), dict()]  # goblins, elves
    walls = set()
    cavern = set()
    max_x, max_y = 0, 0
    for y, row in enumerate(data.splitlines()):
        for x, val in enumerate(row):
            if val == "#":
                walls.add((x, y))
            elif val == "E":
                units[1][(x, y)] = 200
            elif val == "G":
                units[0][(x, y)] = 200
            else:  # val = "."
                cavern.add((x, y))
            max_x = max(max_x, x)
        max_y = max(max_y, y)
    return units, walls, cavern, max_x, max_y


def nn(x, y, forbidden):
    neighbors = list()
    for u, v in ((0, -1), (-1, 0), (1, 0), (0, 1)):
        z = (x + u, y + v)
        if z not in forbidden:
            neighbors.append(z)
    return neighbors


def find_path(start, allowed, neighbors):
    lengths = {start: 0}
    dq = deque([start])
    while dq:
        z = dq.popleft()
        for w in neighbors[z]:
            if w in allowed and w not in lengths:
                lengths[w] = lengths[z] + 1
                dq.append(w)
    return lengths


def combat(units, cavern, neighbors, AP=3):
    elves = len(units[1])
    rounds = 0
    finish = False
    while not finish:
        turns = sorted(units[0] | units[1], key=lambda z: (z[1], z[0]))
        while turns:
            if AP > 3 and len(units[1]) < elves:
                return

            unit = turns.pop(0)

            is_elf = unit in units[1]
            targets = units[1 - is_elf]

            if unit not in units[is_elf]:
                continue

            if not targets:
                finish = True
                break

            # Check if unit is in range of an adjacent target
            in_range_of = list()
            for z in neighbors[unit]:
                if z in targets:
                    in_range_of.append((targets[z], z))

            if in_range_of:
                _, to_attack = min(in_range_of, key=lambda p: (p[0], p[1][1], p[1][0]))
                damage = AP if is_elf else 3
                targets[to_attack] -= damage
                if targets[to_attack] <= 0:
                    cavern.add(to_attack)
                    del targets[to_attack]
                    if to_attack in turns:
                        turns.remove(to_attack)
                continue

            # Get positions in range for all targets
            in_range = list()
            for target in targets:
                in_range += [z for z in neighbors[target] if z in cavern]

            if not in_range:
                continue

            # Get all paths from unit cells in range of target units
            lengths = find_path(unit, cavern, neighbors)
            reachable = [t for t in in_range if t in lengths]
            if not reachable:
                continue
            chosen = min(reachable, key=lambda t: (lengths[t], t[1], t[0]))
            back = find_path(chosen, cavern, neighbors)
            steps = [t for t in neighbors[unit] if t in back]
            move_to = min(steps, key=lambda t: (back[t], t[1], t[0]))
            cavern.remove(move_to)
            cavern.add(unit)
            units[is_elf][move_to] = units[is_elf].pop(unit)

            in_range_of = list()
            for z in neighbors[move_to]:
                if z in targets:
                    in_range_of.append((targets[z], z))

            if in_range_of:
                _, to_attack = min(in_range_of, key=lambda p: (p[0], p[1][1], p[1][0]))
                damage = AP if is_elf else 3
                targets[to_attack] -= damage
                if targets[to_attack] <= 0:
                    cavern.add(to_attack)
                    del targets[to_attack]
                    if to_attack in turns:
                        turns.remove(to_attack)

        else:
            rounds += 1

    return rounds, units


@timer
def part1(data):
    units, walls, cavern, max_x, max_y = parse(data)
    neighbors = {
        (x, y): nn(x, y, walls)
        for (x, y) in product(range(max_x + 1), range(max_y + 1))
    }

    rounds, units = combat(units, cavern, neighbors)
    return rounds * sum(units[len(units[0]) == 0].values())


@timer
def part2(data):
    units, walls, cavern, max_x, max_y = parse(data)
    neighbors = {
        (x, y): nn(x, y, walls)
        for (x, y) in product(range(max_x + 1), range(max_y + 1))
    }

    for AP in count(4):
        result = combat(deepcopy(units), deepcopy(cavern), neighbors, AP=AP)
        if result:
            rounds, units = result
            return rounds * sum(units[len(units[0]) == 0].values())


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2(data))


if __name__ == "__main__":
    main()
