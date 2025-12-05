from copy import deepcopy
import click

from aoc.utils import read_data, timer


def evolve(grid, turns, bursts):
    Lx = int(max(z.real for z in grid)) + 1
    Ly = int(max(z.imag for z in grid)) + 1

    pos = Lx // 2 + 1j * (Ly // 2)
    direction = -1j
    infections = 0
    for _ in range(bursts):
        state = grid.get(pos, ".")
        state, rot = turns[state]
        grid[pos] = state
        direction *= rot
        pos += direction
        infections += state == "#"
    return infections


@timer
def part1(grid, bursts):
    turns = {".": ("#", -1j), "#": (".", 1j)}
    return evolve(grid, turns, bursts)


@timer
def part2(grid, bursts):
    turns = {".": ("W", -1j), "W": ("#", 1), "#": ("F", 1j), "F": (".", -1)}
    return evolve(grid, turns, bursts)


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    grid = dict()
    for y, row in enumerate(data.splitlines()):
        for x, c in enumerate(row):
            grid[x + 1j * y] = c

    # ==== PART 1 ====
    print(part1(deepcopy(grid), 10_000))

    # ==== PART 2 ====
    print(part2(deepcopy(grid), 10_000_000))


if __name__ == "__main__":
    main()
