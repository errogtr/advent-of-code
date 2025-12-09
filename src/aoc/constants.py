from pathlib import Path

# path constants
ROOT_DIR = Path(__file__).parent


# solutions.py template
SOLUTIONS_TEMPLATE = """import click
from aoc.utils import read_data, timer


@timer
def part1():
    pass


@timer
def part2():
    pass


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1())

    # ==== PART 2 ====
    print(part2())


if __name__ == "__main__":
    main()

"""
