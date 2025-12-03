from math import ceil, floor

from aoc.utils import read_data


def validate(id_ranges: list[tuple[int, int]], max_reps: int) -> int:
    invalid = set()
    for L, R in id_ranges:
        # - find all numbers n s.t. n n ... n (k times) is inside [L, R]
        #
        # - all numbers of the form n n ... n with k digits can be written as
        #       n * M(k, d)
        #   where M(k, d) = (10 ** (d * k) - 1) // (10**d - 1)
        #   e.g. M(3, 2) = 1001
        #        M(2, 2) = 101
        #
        # - the invalid numbers inside the range are thus:
        #       L <= n * M(k, d) <= R
        #
        for k in range(max_reps, 1, -1):
            min_digits = max(1, len(str(L)) // k)
            max_digits = len(str(R)) // k
            for d in range(min_digits, max_digits + 1):
                M = (10 ** (d * k) - 1) // (10**d - 1)

                # n must have d digits, so it cannot exceed [10 ** (d - 1), 10**d - 1]
                n_low = max(ceil(L / M), 10 ** (d - 1))
                n_high = min(floor(R / M), 10**d - 1)
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
    print(validate(id_ranges, max_reps=2))

    # ==== PART 2 ====
    print(validate(id_ranges, max_reps=max_len))


if __name__ == "__main__":
    main()
