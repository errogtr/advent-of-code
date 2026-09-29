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
    
    path = [end]
    while True:
        move_to = came_from[path[-1]]
        if move_to == start:
            break
        path.append(move_to)
    return length, path


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
    # print_grid(elves, goblins, walls)
    neighbors = {z: nn(*z) for z in set(elves) | set(goblins) | cavern}
    rounds = 0
    finish = False
    while True:
        for unit in sorted(elves | goblins, key=lambda z: (z[1], z[0])):
            elves = {z: hp for z, hp in elves.items() if hp > 0}
            goblins = {z: hp for z, hp in goblins.items() if hp > 0}
            if unit not in elves | goblins:
                continue
            
            is_elf = unit in elves
            targets = goblins if is_elf else elves

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
                targets[to_attack] -= 3
                if targets[to_attack] <= 0:
                    cavern.add(to_attack)
                continue
            
            # Get positions in range for all targets
            in_range = list()
            for target in targets:
                in_range += [z for z in neighbors[target] if z in cavern]
            
            if not in_range:
                continue

            # Get all paths from unit to target units
            print("Round:", rounds, "; ", "Unit:", unit)
            paths = list()
            for target in in_range:
                path = find_paths(unit, target, cavern, neighbors)
                if path:
                    paths.append(path)
            print("Path trovati: ", len(paths))
            
            if not paths:
                continue

            if len(paths) > 1:
                pass

            _, min_path = min(paths, key=lambda p: (p[0], p[1][0][1], p[1][0][0]))
            move_to = min_path[-1]
            cavern.remove(move_to)
            cavern.add(unit)
            if is_elf:
                elves[move_to] = elves.pop(unit)
            else:  # is_goblin
                goblins[move_to] = goblins.pop(unit)

            in_range_of = list()
            for z in neighbors[move_to]:
                if z in targets:
                    in_range_of.append((targets[z], z))
            
            if in_range_of:
                _, to_attack = min(in_range_of, key=lambda p: (p[0], p[1][1], p[1][0]))
                targets[to_attack] -= 3
                if targets[to_attack] <= 0:
                    cavern.add(to_attack)

        # print_grid(elves, goblins, walls)
        if finish:
            break

        rounds += 1


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
    if example:
        for ex in data.split("\n\n"):
            data = "\n".join(ex.splitlines()[:-1])
            ans = int(ex.splitlines()[-1])
            print(part1(data)==ans)
    else:
        print(part1(data))

    # ==== PART 2 ====
    print(part2())


if __name__ == "__main__":
    main()
