from math import inf
from pathlib import Path


NN_MAP = {
    "n": (0, 1, -1),
    "s": (0, -1, 1),
    "ne": (1, 0, -1),
    "sw": (-1, 0, 1),
    "se": (1, -1, 0),
    "nw": (-1, 1, 0),
}


def hex_dist(q, r, s):
    return (abs(q) + abs(r) + abs(s)) // 2


def main(input_path: Path):
    """
    Implemented using cube coordinates for hexagons.
    Source: https://www.redblobgames.com/grids/hexagons/
    """

    with input_path.open() as f:
        steps = f.read().split(",")

    q, r, s = 0, 0, 0
    max_dist = -inf
    for step in steps:
        dq, dr, ds = NN_MAP[step]
        q, r, s = q + dq, r + dr, s + ds
        max_dist = max(max_dist, hex_dist(q, r, s))

    # ==== PART 1 ====
    print(hex_dist(q, r, s))

    # ==== PART 2 ====
    print(max_dist)
