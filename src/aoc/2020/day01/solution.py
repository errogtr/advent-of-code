from itertools import combinations
import click
from aoc.utils import read_data, timer


@timer
def part1(report):
    return next(x * y for x, y in combinations(report, 2) if x + y == 2020)


@timer
def part2(report):
    return next(x * y * z for x, y, z in combinations(report, 3) if x + y + z == 2020)


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    report = [int(x) for x in data.splitlines()]

    # ==== PART 1 ====
    print(part1(report))

    # ==== PART 2 ====
    print(part2(report))


if __name__ == "__main__":
    main()
