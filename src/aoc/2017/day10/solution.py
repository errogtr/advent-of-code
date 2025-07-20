from functools import reduce
from itertools import batched
from operator import xor
from pathlib import Path


def single_round(lengths, n, nums, pos, skip):
    for length in lengths:
        slice = [nums[(pos + i) % n] for i in range(length)]
        for i in range(length):
            nums[(pos + i) % n] = slice[-i - 1]
        pos += length + skip
        skip += 1
    return nums, pos, skip


def main(input_path: Path):
    with input_path.open() as f:
        inputs = f.read()

    n = 256

    # ==== PART 1 ====
    lengths = [int(x) for x in inputs.split(",")]
    nums, pos, skip = single_round(lengths, n, list(range(n)), 0, 0)
    print(nums[0] * nums[1])

    # ==== PART 2 ====
    lengths = [ord(c) for c in inputs] + [17, 31, 73, 47, 23]
    nums, pos, skip = list(range(n)), 0, 0
    for _ in range(64):
        nums, pos, skip = single_round(lengths, n, nums, pos, skip)

    knot_hash = "".join(f"{reduce(xor, block):02x}" for block in batched(nums, 16))

    print(knot_hash)
