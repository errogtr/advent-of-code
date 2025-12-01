from pathlib import Path


def parse(line: str) -> tuple[str, int]:
    direction, amount = line[0], line[1:]
    return direction, int(amount)


def main(input_path: Path):
    with input_path.open() as f:
        rotations = [parse(line) for line in f.read().splitlines()]

    # ==== PART 1 ====
    pos = 50
    zeroes = 0
    for direction, amount in rotations:
        sign = (-1) ** (direction == "L")
        pos = (pos + sign * amount) % 100
        if pos == 0:
            zeroes += 1

    print(zeroes)


    # ==== PART 2 ====
    pos = 50
    zeroes = 0
    for direction, amount in rotations:
        sign = (-1) ** (direction == "L")
        new_pos = pos + sign * amount
        if new_pos >= 100:
            zeroes += new_pos // 100
        elif new_pos == 0:
            zeroes += 1
        elif new_pos < 0:
            zeroes += - (new_pos // 100)
            if pos == 0:
                zeroes -= 1
            if new_pos % 100 == 0:
                zeroes += 1

        pos = new_pos % 100
        
    print(zeroes)
