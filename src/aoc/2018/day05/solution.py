import string
import click
from aoc.utils import read_data, timer


def react(polymer):
    stack = []
    for unit in polymer:
        if stack and stack[-1] != unit and stack[-1].lower() == unit.lower():
            stack.pop()
        else:
            stack.append(unit)
    return "".join(stack)


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
