from math import prod
import click

from aoc.utils import read_data, timer


# The area of every shape summed up should not be too high compared
# to the available space. I have no idea why COEFF=1.0 works, but below
# this value I got wrong solutions...
COEFF = 1.0


@timer
def part1(data):
    *presents_list, region_specs = data.split("\n\n")

    shapes = [present.count("#") for present in presents_list]

    fit = 0
    for specs in region_specs.splitlines():
        shape, counter = specs.split(": ")
        area = prod(map(int, shape.split("x")))
        counts = [int(x) for x in counter.split()]
        fit += area >= COEFF * sum(shapes[i] * c for i, c in enumerate(counts))

    return fit


@timer
def part2():
    pass


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2())


if __name__ == "__main__":
    main()
