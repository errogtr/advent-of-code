import click

from aoc.utils import read_data, timer


@timer
def part1():
    pass


@timer
def part2():
    pass


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    instructions = data.splitlines()

    # ==== PART 1 ====
    print(part1())

    # ==== PART 2 ====
    print(part2())


if __name__ == "__main__":
    main()
