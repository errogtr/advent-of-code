from itertools import product
import json
from math import ceil, floor
from pathlib import Path
import re


def add(x: str, y: str) -> str:
    return f"[{x},{y}]"


def reduce(x: str) -> str:
    while True:
        # check for possible explosions
        for m in re.finditer(r"\[(\d+),(\d+)\]", x):
            before_m = x[: m.start()]
            after_m = x[m.end() :]
            if before_m.count("[") - before_m.count("]") == 4:
                x = explode(x, m.groups(), before_m, after_m)
                break
        else:
            # check for leftmost split
            if m := re.search(r"\d{2,}", x):
                x = split(x, m)
            else:
                break
    return x


def explode(x: str, snailfish: tuple[str, str], before: str, after: str) -> str:
    snailfish_left, snailfish_right = map(int, snailfish)

    # add left snailfish value to first regular number at its left, if any
    add_left = None
    for n in re.finditer(r"\d+", before):
        add_left = n

    if add_left:
        to_add = int(add_left.group())
        x = f"{before[:add_left.start()]}{to_add + snailfish_left}{before[add_left.end():]}"
    else:
        x = before

    # replace exploded snailfish number with 0
    x += "0"

    # add right snailfish value to first regular number at its right, if any
    add_right = re.search(r"(\d+)", after)
    if add_right:
        to_add = int(add_right.group())
        x += f"{after[:add_right.start()]}{snailfish_right + to_add}{after[add_right.end():]}"
    else:
        x += after

    return x


def split(x: str, m: re.Match) -> str:
    half = int(m.group()) / 2
    return x[: m.start()] + f"[{floor(half)},{ceil(half)}]" + x[m.end() :]


def magnitude(x: str) -> int:
    return pair_magnitude(json.loads(x))


def pair_magnitude(snailfish: list) -> int:
    left, right = snailfish
    m = 3 * pair_magnitude(left) if isinstance(left, list) else 3 * left
    m += 2 * pair_magnitude(right) if isinstance(right, list) else 2 * right
    return m


def main(input_path: Path):
    with input_path.open() as f:
        snailfishes = f.read().splitlines()

    # ==== PART 1 ====
    x, *others = snailfishes
    for y in others:
        x = reduce(add(x, y))
    print(magnitude(x))

    # ==== PART 2 ====
    print(max(magnitude(reduce(add(x, y))) for x, y in product(snailfishes, repeat=2)))
