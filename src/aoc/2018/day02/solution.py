from collections import Counter
from itertools import combinations


import click
from aoc.utils import read_data, timer


def hamming(X, Y):
    return sum(x != y for x, y in zip(X, Y))


@timer
def part1(box_ids: list[str]) -> int:
    twice = 0
    thrice = 0
    for box_id in box_ids:
        c = Counter(box_id)
        twice += 2 in c.values()
        thrice += 3 in c.values()

    return twice * thrice


@timer
def part2(box_ids: list[str]) -> str:
    for X, Y in combinations(box_ids, 2):
        if hamming(X, Y) == 1:
            return "".join(c_X for c_X, c_Y in zip(X, Y) if c_X == c_Y)
    raise ValueError("No box ids pair has Hamming distance = 1")


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    box_ids = data.splitlines()

    # ==== PART 1 ====
    print(part1(box_ids))

    # ==== PART 2 ====
    print(part2(box_ids))


if __name__ == "__main__":
    main()
