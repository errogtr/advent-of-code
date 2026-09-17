from collections import Counter
from itertools import product
import re
import click
from aoc.utils import read_data, timer


@timer
def part12(data):
    patches = list()
    for claim in data.splitlines():
        m = re.match(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$", claim)
        c, x, y, w, h = map(int, m.groups())
        patches.append((c, x, y, w, h))

    fabric = Counter()
    for pc, px, py, pw, ph in patches:
        for x, y in product(range(px, px + pw), range(py, py + ph)):
            fabric[(x, y)] += 1

    intact = next(
        pc
        for pc, px, py, pw, ph in patches
        if all(
            fabric[(x, y)] == 1
            for x, y in product(range(px, px + pw), range(py, py + ph))
        )
    )

    return sum(c > 1 for c in fabric.values()), intact


@timer
def part2():
    pass


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 & 2====
    print(part12(data))


if __name__ == "__main__":
    main()
