from copy import copy
import heapq
import click
from aoc.utils import read_data, timer


def parse(data):
    elves = dict()
    goblins = dict()
    walls = set()
    cavern = set()
    for y, row in enumerate(data.splitlines()):
        for x, val in enumerate(row):
            if val == "#":
                walls.add((x, y))
            elif val == "E":
                elves[(x, y)] = 200
            elif val == "G":
                goblins[(x, y)] = 200
            else:  # val = "."
                cavern.add((x, y))
    return elves, goblins, walls, cavern


def nn(x, y):
    return ((x, y - 1), (x + 1, y), (x, y + 1), (x-1, y))


def find_paths(start, end, allowed, neighbors):
    visited = {start}
    queue = [(0, start)]
    came_from = {start: None}
    length = 0
    is_blocked = True
    while queue:
        length, z = heapq.heappop(queue)

        if z == end:
            is_blocked = False
            break

        for w in neighbors[z]:
            if w in allowed - visited:
                visited.add(w)
                heapq.heappush(queue, (length + 1, w))
                came_from[w] = z

    if is_blocked:
        return None
    
    current = end
    while True:
        move_to = came_from[current]
        if move_to == start:
            break
        current = move_to
    return length, current


def print_grid(elves, goblins, walls):
    points = set(elves) | set(goblins) | walls
    max_x, max_y = map(max, zip(*points))

    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in elves:
                grid[y][x] = "E"
            elif (x, y) in goblins:
                grid[y][x] = "G"
            elif (x, y) in walls:
                grid[y][x] = "#"
    
    print(chr(27) + "[2J")
    print("\n".join("".join(row) for row in grid))



@timer
def part1(data):
    elves, goblins, walls, cavern = parse(data)
    print_grid(elves, goblins, walls)
    neighbors = {z: nn(*z) for z in set(elves) | set(goblins) | cavern}
    rounds = 0
    while True:
        next_goblins = copy(goblins)
        next_cavern = copy(cavern)
        next_elves = copy(elves)
        for unit in sorted(elves | goblins, key=lambda z: (z[1], z[0])):
            is_elf = unit in elves
            targets = next_goblins if is_elf else next_elves

            if not targets:
                break

            # Check if unit is in range of an adjacent target
            in_range_of = None
            for z in neighbors[unit]:
                if z in targets:
                    in_range_of = z
                    break
            
            if in_range_of:  # attack
                targets[in_range_of] -= 3
                continue
            
            # Get positions in range for all targets
            in_range = list()
            for target in targets:
                in_range += [z for z in neighbors[target] if z in cavern]
            
            if not in_range:
                continue

            # Get all paths from unit to target units
            if unit == (3, 4):
                pass
            paths = list()
            for target in in_range:
                path = find_paths(unit, target, cavern, neighbors)
                if path:
                    paths.append(path)
            
            if not paths:
                continue

            _, move_to = min(paths, key=lambda p: (p[0], p[1][1], p[1][0]))
            next_cavern.remove(move_to)
            next_cavern.add(unit)
            if is_elf:
                next_elves[move_to] = next_elves.pop(unit)
            else:  # is_goblin
                next_goblins[move_to] = next_goblins.pop(unit)

            print_grid(next_elves, next_goblins, walls)
            pass

        next_elves = {z: hp for z, hp in next_elves.items() if hp > 0}
        next_goblins = {z: hp for z, hp in next_goblins.items() if hp > 0}
        if len(next_goblins) == 0 or len(next_elves) == 0:
            break
        rounds += 1

        goblins = next_goblins
        elves = next_elves
        cavern = next_cavern

        if rounds in (1, 2, 23, 24, 25, 26, 27, 28, 48):
            pass
        # if rounds in (0, 1, 22, 23, 24, 25, 26, 27, 47):
        #     pass

    if elves:
        outcome = rounds * sum(elves.values())
    else:
        outcome = rounds * sum(goblins.values())
    return outcome
        


@timer
def part2():
    pass


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2())


if __name__ == "__main__":
    main()
