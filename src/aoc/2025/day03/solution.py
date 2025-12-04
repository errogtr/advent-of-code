import click
from aoc.utils import read_data, timer


def total_joltage(data, seq_len):
    total = 0
    for bank in data.split("\n"):
        joltage = ""
        start, end = 0, len(bank) - seq_len + 1
        for i in range(seq_len):
            window = bank[start : end + i]
            m = max(window)
            joltage += m
            start += window.find(m) + 1
        total += int(joltage)

    return total


@timer
def part1(data):
    return total_joltage(data, 2)


@timer
def part2(data):
    return total_joltage(data, 12)


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
