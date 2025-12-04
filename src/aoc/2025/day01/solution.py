import click
from aoc.utils import read_data, timer


def parse(line: str) -> tuple[str, int]:
    direction, amount = line[0], line[1:]
    return (-1) ** (direction == "L"), int(amount)


@timer
def part1(rotations):
    pos = 50
    zeroes = 0
    for direction, amount in rotations:
        pos = (pos + direction * amount) % 100
        zeroes += pos == 0
    return zeroes


@timer
def part2(rotations):
    pos = 50
    zeroes = 0
    for direction, amount in rotations:
        turns, rot = divmod(amount, 100)
        zeroes += turns
        new_pos = pos + direction * rot

        if new_pos >= 100 or (pos > 0 and new_pos <= 0):
            zeroes += 1

        pos = new_pos % 100
    return zeroes


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)
    rotations = [parse(line) for line in data.splitlines()]

    # ==== PART 1 ====
    print(part1(rotations))

    # ==== PART 2 ====
    print(part2(rotations))


if __name__ == "__main__":
    main()
