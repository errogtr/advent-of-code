from itertools import cycle

import click
from aoc.utils import read_data, timer


@timer
def part1(frequency_changes: list[int]) -> int:
    return sum(frequency_changes)


@timer
def part2(frequency_changes: list[int]) -> int:
    frequency = 0
    frequencies = {frequency}
    for change in cycle(frequency_changes):
        frequency += change
        if frequency in frequencies:
            break
        frequencies.add(frequency)
    return frequency


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    frequency_changes = [int(line) for line in data.splitlines()]

    # ==== PART 1 ====
    print(part1(frequency_changes))

    # ==== PART 2 ====
    print(part2(frequency_changes))


if __name__ == "__main__":
    main()
