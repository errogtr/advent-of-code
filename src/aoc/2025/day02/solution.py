from math import ceil
from pathlib import Path


def validate(id_ranges: list[tuple[int, int]], max_len: int, max_groups: int) -> int:
    invalid = set()
    for k in range(2, max_groups + 1):
        for n in range(10 ** ceil(max_len / k)):
            rep = int(str(n) * k)
            for l, r in id_ranges:
                if l <= rep <= r:
                    invalid.add(rep)
    return sum(invalid)


def main(input_path: Path):
    with input_path.open() as f:
        data = f.read()

    max_len = 0  # max digits number
    id_ranges = list()  # list of int ranges [(lower bound, upper bound)]
    for id_range in data.split(","):
        low, up = id_range.split("-")
        max_len = max(max_len, len(up))
        id_ranges.append((int(low), int(up)))

    # ==== PART 1 ====
    print(validate(id_ranges, max_len, max_groups=2))

    # ==== PART 2 ====
    print(validate(id_ranges, max_len, max_groups=max_len))
