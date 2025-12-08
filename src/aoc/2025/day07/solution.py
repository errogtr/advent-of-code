from collections import Counter

import click

from aoc.utils import read_data, timer


@timer
def part1(start, splitters):
    splits = 0
    beam = {start}
    for row_splitters in splitters:
        for splitter in row_splitters & beam:
            beam.remove(splitter)
            beam |= {splitter - 1, splitter + 1}
            splits += 1
    return splits


@timer
def part2(start, splitters):
    beam = Counter({start: 1})
    for row_splitters in splitters:
        for splitter in row_splitters & set(beam):
            beam[splitter - 1] += beam[splitter]
            beam[splitter + 1] += beam[splitter]
            beam[splitter] = 0
    return beam.total()


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    first_row, *rows = data.splitlines()
    start = first_row.index("S")
    splitters = [{x for x, c in enumerate(row) if c == "^"} for row in rows]

    # ==== PART 1 ====
    print(part1(start, splitters))

    # ==== PART 2 ====
    print(part2(start, splitters))


if __name__ == "__main__":
    main()
