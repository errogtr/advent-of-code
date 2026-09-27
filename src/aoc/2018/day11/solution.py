from itertools import product
import click
from aoc.utils import read_data, timer


def cell(x, y, serial):
    if x == 0 or y == 0:
        return 0
    return (((x + 10) * (serial + y * (x + 10)) // 100) % 10) - 5


def summed_area_table(serial):
    cells = [[cell(x, y, serial) for x in range(301)] for y in range(301)]
    for x, y in product(range(1, 301), range(1, 301)):
        cells[y][x] += cells[y][x - 1] + cells[y - 1][x] - cells[y - 1][x - 1]
    return cells


def max_power_block(cells, sizes):
    best = None
    max_power = 0
    for size in sizes:
        for x, y in product(range(1, 302 - size), repeat=2):
            power = (
                cells[y - 1][x - 1]
                - cells[y - 1][x + size - 1]
                - cells[y + size - 1][x - 1]
                + cells[y + size - 1][x + size - 1]
            )
            if power > max_power:
                max_power = power
                best = x, y, size
    return best


@timer
def part1(data):
    """Using summed-area table method with a fixed-size 3x3 window
    --> https://en.wikipedia.org/wiki/Summed-area_table
    """
    x, y, _ = max_power_block(summed_area_table(int(data)), [3])
    return f"{x},{y}"


@timer
def part2(data):
    """Using summed-area table method with variable size window"""
    x, y, size = max_power_block(summed_area_table(int(data)), range(1, 301))
    return f"{x},{y},{size}"


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
