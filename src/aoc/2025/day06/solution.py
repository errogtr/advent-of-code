from math import prod
import click
from aoc.utils import read_data, timer


OPS = {"+": sum, "*": prod}


@timer
def part1(data):
    rows = [r.split() for r in data.splitlines()]

    total = 0
    for col in zip(*rows):
        *nums, op = col
        total += OPS[op](map(int, nums))
    return total


@timer
def part2(data):
    *num_rows, ops_row = data.splitlines()
    nums_right_to_left = [r[::-1] for r in num_rows]
    l_rows = len(num_rows)

    num_blocks = list()
    current_block = list()
    for col in zip(*nums_right_to_left):
        digits = "".join(col)
        if digits.count(" ") == l_rows:
            num_blocks.append(current_block)
            current_block = list()
        else:
            current_block.append(int(digits))

    num_blocks.append(current_block)

    ops_right_to_left = [OPS[op] for op in ops_row.split()[::-1]]

    return sum(op(block) for op, block in zip(ops_right_to_left, num_blocks))


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2(data))


if __name__ == "__main__":
    main()
