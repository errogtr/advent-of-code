from collections import Counter

import click

from aoc.utils import read_data, timer


@timer
def part1(start, splitters):
    splits = 0
    beam = {start}
    for row_splitters in splitters[1:]:
        beam = {z + 1j for z in beam}
        for splitter in row_splitters & beam:
            beam.remove(splitter)
            beam |= {splitter - 1, splitter + 1}
            splits += 1
    return splits


@timer
def part2(start, splitters):
    beam = Counter({start: 1})
    for row_splitters in splitters[1:]:
        beam = Counter({z + 1j: count for z, count in beam.items()})
        for splitter in row_splitters & set(beam):
            beam[splitter - 1] += beam[splitter]
            beam[splitter + 1] += beam[splitter]
            beam[splitter] = 0
    return beam.total()


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    rows = data.splitlines()
    start = next(x for x, c in enumerate(rows[0]) if c == "S")

    splitters = list()
    for y, row in enumerate(rows[1:]):
        row_splitters = set()
        for x, c in enumerate(row):
            z = x + 1j * y
            if c == "S":
                start = z
            elif c == "^":
                row_splitters.add(z)
        splitters.append(row_splitters)

    # ==== PART 1 ====
    print(part1(start, splitters))

    # ==== PART 2 ====
    print(part2(start, splitters))


if __name__ == "__main__":
    main()
