from itertools import count
import re

import click

from aoc.utils import read_data, timer


def parse(line: str) -> tuple[int, int]:
    positions_match = re.search(r"(\d+) positions.+position (\d+)", line)
    period, start = map(int, positions_match.groups())
    return period, start


def min_alignment_time(discs):
    first_disc, *other_discs = discs
    first_disc_period, first_disc_start = first_disc
    for k in count(1):
        t = first_disc_period * k - first_disc_start

        exit_conditions = [
            (t + delta_t + start) % period == 0
            for delta_t, (period, start) in enumerate(other_discs, 1)
        ]

        if all(exit_conditions):
            return t - 1


@timer
def part1(discs):
    return min_alignment_time(discs)


@timer
def part2(discs):
    return min_alignment_time(discs + [(11, 0)])


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    discs = [parse(line) for line in data.splitlines()]

    # ==== PART 1 ====
    print(part1(discs))

    # ==== PART 2 ====
    print(part2(discs))


if __name__ == "__main__":
    main()
