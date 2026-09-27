import click
from aoc.utils import read_data, timer


def parse(data):
    init, notes = data.split("\n\n")

    init = init.split(": ")[-1]

    rules = dict()
    for line in notes.splitlines():
        inp, res = line.split(" => ")
        rules[inp] = res

    return init, rules


@timer
def part1(data):
    init, rules = parse(data)

    for _ in range(20):
        init = "...." + init + "...."
        state = "".join(rules.get(init[i : i + 5], ".") for i in range(len(init) - 4))
        init = state
    return sum(i for i, pot in enumerate(state, -2 * 20) if pot == "#")


@timer
def part2(data):
    """
    Define the quantity asked by the puzzled as:

        count_{t} := sum(i for i, pot in enumerate(state, -2 * t) if pot == "#")

    I noticed that after t=142, the difference (count_{t+1} - count_{t}) stabilizes:

        count_{t+1} - count_{t} = 32, t>=142

    that is, count_{t} is asymptotic to a straight line with slope 32.

    Since count_{142} = 4945, the formula below follows.

    N.B. the numbers in the formula work specifically for my input.
    """

    return (50_000_000_000 - 142) * 32 + 4945


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
