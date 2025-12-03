from math import ceil

from aoc.utils import read_data


def validate(id_ranges: list[tuple[int, int]], max_groups: int) -> int:
    invalid = set()

    for L, R in id_ranges:
        for k in range(max_groups, 1, -1):
            min_digits = max(1, len(str(L)) // k)
            max_digits = len(str(R)) // k
            for d in range(min_digits, max_digits + 1):
                M = (10 ** (d * k) - 1) // (10**d - 1)

                nd_low = 10 ** (d - 1)
                nd_high = 10**d - 1

                # Intersect with digit-range of n
                n_low = max(ceil(L / M), nd_low)
                n_high = min(R // M, nd_high)

                invalid |= set(n * M for n in range(n_low, n_high + 1))

    return sum(invalid)


def main():
    data = read_data(__file__)

    max_len = 0  # max digits number
    id_ranges = list()  # list of int ranges [(lower bound, upper bound)]
    for id_range in data.split(","):
        low, up = id_range.split("-")
        max_len = max(max_len, len(up))
        id_ranges.append((int(low), int(up)))

    # ==== PART 1 ====
    print(validate(id_ranges, max_groups=2))

    # ==== PART 2 ====
    print(validate(id_ranges, max_groups=max_len))


if __name__ == "__main__":
    main()
