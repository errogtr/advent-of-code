from collections import defaultdict
import re
import click

from aoc.utils import read_data, timer


def parse_state(instructions):
    """
    returns {
        0: (
            value to write if current=0,
            direction if current=0,
            next state if current=0
        ),
        1: (
            value to write if current=1,
            direction if current=1,
            next state if current=1
        )
    }
    """
    return {
        ctrl: (
            int(re.search(r"(\d+)", instructions[k + 2]).group(1)),
            1 if "right" in instructions[k + 3] else -1,
            re.search(r"([A-F])\.", instructions[k + 4]).group(1),
        )
        for ctrl, k in [(0, 0), (1, 4)]
    }


@timer
def part1(data):
    instructions = data.splitlines()
    state_instructions = {
        state: parse_state(instructions[idx : idx + 10])
        for state, idx in zip("ABCDEF", range(3, len(instructions), 10))
    }

    state = re.search(r"state (\w)", instructions[0]).group(1)
    steps = re.search(r"\d+", instructions[1]).group(0)

    tape = defaultdict(int)
    offset = 0
    for _ in range(int(steps)):
        cursor = tape[offset]
        write_val, move_to, state = state_instructions[state][cursor]
        tape[offset] = write_val
        offset += move_to

    return sum(tape.values())


@timer
def part2():
    return "Merry Christmas!"


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2())


if __name__ == "__main__":
    main()
