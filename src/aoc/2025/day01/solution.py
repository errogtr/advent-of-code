from pathlib import Path

from aoc.utils import read_data


def parse(line: str) -> tuple[str, int]:
    direction, amount = line[0], line[1:]
    return (-1) ** (direction == "L"), int(amount)


def main():
    data = read_data(__file__)
    rotations = [parse(line) for line in data.splitlines()]

    # ==== PART 1 ====
    pos = 50
    zeroes = 0
    for direction, amount in rotations:
        pos = (pos + direction * amount) % 100
        zeroes += pos == 0

    print(zeroes)

    # ==== PART 2 ====
    pos = 50
    zeroes = 0
    for direction, amount in rotations:
        turns, rot = divmod(amount, 100)
        zeroes += turns
        new_pos = pos + direction * rot

        if new_pos >= 100 or (pos > 0 and new_pos <= 0):
            zeroes += 1

        pos = new_pos % 100

    print(zeroes)


if __name__ == "__main__":
    main()
