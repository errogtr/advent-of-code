from collections import Counter
from pathlib import Path


def main(input_path: Path):
    with input_path.open() as f:
        locations = [[int(x) for x in l.split()] for l in f.readlines()]

    # ==== PART 1 ====
    left_locs, right_locs = zip(*locations)
    print(sum(abs(l - r) for l, r in zip(sorted(left_locs), sorted(right_locs))))

    # ==== PART 2 ====
    c = Counter(right_locs)
    print(sum(l * c[l] for l in left_locs))
