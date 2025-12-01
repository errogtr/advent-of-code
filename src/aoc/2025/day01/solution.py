from pathlib import Path


def parse(line: str) -> tuple[str, int]:
    direction, amount = line[0], line[1:]
    return (-1) ** (direction == "L"), int(amount)


def main(input_path: Path):
    with input_path.open() as f:
        rotations = [parse(line) for line in f.read().splitlines()]

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
