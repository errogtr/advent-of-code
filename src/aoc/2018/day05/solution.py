import string
import click
from aoc.utils import read_data, timer


# fmt: off
reactions = {
    'aA', 'bB', 'cC', 'dD', 'eE', 'fF', 'gG', 'hH', 'iI', 'jJ', 'kK', 'lL', 'mM', 
    'nN', 'oO', 'pP', 'qQ', 'rR', 'sS', 'tT', 'uU', 'vV', 'wW', 'xX', 'yY', 'zZ',
    'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 
    'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz',
    }
# fmt: on


def react(polymer):
    i = 0
    while i < len(polymer):
        if polymer[i : i + 2] in reactions:
            polymer = polymer[:i] + polymer[i + 2 :]
            i -= 1
        else:
            i += 1
    return polymer


@timer
def part1(polymer):
    return len(react(polymer))


@timer
def part2(polymer):
    shortest = len(polymer)
    polymer = react(polymer)
    for unit in string.ascii_lowercase:
        modified = polymer.replace(unit, "").replace(unit.upper(), "")
        shortest = min(shortest, len(react(modified)))
    return shortest


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2(data))


if __name__ == "__main__":
    main()
