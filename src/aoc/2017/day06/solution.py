from copy import copy
from pathlib import Path


def distribute(blocks: list[int]) -> list[int]:
    new_blocks = copy(blocks)
    max_val = max(new_blocks)
    i = new_blocks.index(max_val)
    new_blocks[i] = 0
    while max_val:  # I think this can be optimized
        i = (i + 1) % len(new_blocks)
        new_blocks[i] += 1
        max_val -= 1
    return new_blocks


def main(input_path: Path):
    with input_path.open() as f:
        blocks = [int(x) for x in f.read().split()]

    # floyd's algoritm for cycle detection: https://tinyurl.com/35xmkz9p
    slow = fast = blocks
    cycle = 0
    while True:
        slow = distribute(slow)
        fast = distribute(distribute(fast))
        cycle += 1
        if slow == fast:
            break

    fast = blocks
    offset = 1
    while slow != fast:
        slow = distribute(slow)
        fast = distribute(fast)
        offset += 1
        if slow == fast:
            break

    # ==== PART 1 ====
    print(offset + cycle)

    # ==== PART 2 ====
    print(cycle)
