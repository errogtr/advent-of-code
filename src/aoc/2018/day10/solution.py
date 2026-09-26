from itertools import count
import re
from statistics import variance

import click
from aoc.utils import read_data, timer


def parse(data):
    pos = list()
    vel = list()
    for note in data.splitlines():
        px, py, vx, vy = map(int, re.findall(r"(-?\d+)", note))
        pos.append((px, py))
        vel.append((vx, vy))
    return pos, vel


def evolve(data, print_t=False):
    pos, vel = parse(data)
    var_y = variance(y for _, y in pos)
    for t in count(1):
        pos_t = list()
        for (x, y), (vx, vy) in zip(pos, vel):
            pos_t.append((x + vx, y + vy))
        
        var_y_t = variance(y for _, y in pos_t)

        # The message appears when points are less spread along the y-axis
        # than in any other configuration
        if var_y_t > var_y:
            break

        var_y = var_y_t
        pos = pos_t

    # The break condition becomes true one time step after the message
    # appears, so we print t - 1 to correct for that off-by-one.
    if print_t: 
        return t - 1
    
    return visualize(pos)


def visualize(pos):
    pos_x, pos_y = zip(*pos)

    min_x, max_x = min(pos_x), max(pos_x)
    min_y, max_y = min(pos_y), max(pos_y)

    grid = [["." for _ in range(min_x, max_x+1)] for _ in range(min_y, max_y+1)]
    for x, y in pos:
        grid[y-min_y][x-min_x] = "#"
    
    return "\n".join("".join(row) for row in grid)


@timer
def part1(data):
    return evolve(data)
        

@timer
def part2(data):
    return evolve(data, print_t=True)


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

