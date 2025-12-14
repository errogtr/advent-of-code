from math import prod

import click
from aoc.utils import read_data, timer


def trees(slope_x, slope_y, height, width, trees_map):
    trees_count = 0
    x, y = [0, 0]
    while y < height:
        if trees_map[(x % width, y)] == "#":
            trees_count += 1
        x += slope_x
        y += slope_y
    return trees_count


@timer
def part1(height, width, trees_map):
    return trees(3, 1, height, width, trees_map)


@timer
def part2(height, width, trees_map):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    n_trees = [
        trees(slope_x, slope_y, height, width, trees_map) for slope_x, slope_y in slopes
    ]
    return prod(n_trees)


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    lines = data.splitlines()
    trees_map = {(x, y): v for y, line in enumerate(lines) for x, v in enumerate(line)}
    height = len(lines)
    width = len(lines[0])

    # ==== PART 1 ====
    print(part1(height, width, trees_map))

    # ==== PART 2 ====
    print(part2(height, width, trees_map))


if __name__ == "__main__":
    main()
