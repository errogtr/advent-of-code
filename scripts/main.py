from importlib import import_module
import click

from aoc.constants import ROOT_DIR
from aoc.models import Args


@click.command()
@click.argument("year")
@click.argument("day")
@click.option("--example", is_flag=True)
def main(year: int, day: int, example: bool):
    args = Args(year=year, day=day)
    puzzle_module = import_module(args.get_puzzle_module())
    puzzle_module.main(args.get_input_path(root=ROOT_DIR, is_example=example))


if __name__ == "__main__":
    main()
