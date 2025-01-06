from heapq import heappop, heappush
from itertools import product
from math import inf
from pathlib import Path


Coords = tuple[int, int]
Map = dict[Coords, int]


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def parse(input_text: str) -> tuple[Map, int, int]:
    input_lines = input_text.split()
    Lx = len(input_lines[0])
    Ly = len(input_lines)

    riskmap = dict()
    for y, row in enumerate(input_lines):
        for x, val in enumerate(row):
            riskmap[x, y] = int(val)
    return riskmap, Lx, Ly


def get_nns(x: int, y: int) -> list[Coords]:
    return [(x + dx, y + dy) for (dx, dy) in DIRS]


def lowest_risk(riskmap: Map, Lx: int, Ly: int) -> int:
    all_nns = {(x, y): get_nns(x, y) for x, y in riskmap}

    risk = 0
    start = (0, 0)
    end = (Lx - 1, Ly - 1)
    queue = [(risk, *start)]
    visited = {(start)}
    while queue:
        risk, curr_x, curr_y = heappop(queue)

        if (curr_x, curr_y) == end:
            break

        for next_x, next_y in all_nns[curr_x, curr_y]:
            if (next_x, next_y) not in visited:
                next_risk = risk + riskmap.get((next_x, next_y), inf)
                heappush(queue, (next_risk, next_x, next_y))
                visited.add((next_x, next_y))

    return risk


def enlarge(riskmap: Map, Lx: int, Ly: int) -> Map:
    riskmap_enlarged = dict()
    for x_large, y_large in product(range(5 * Lx), range(5 * Ly)):
        x_r, x = divmod(x_large, Lx)
        y_r, y = divmod(y_large, Ly)
        riskmap_enlarged[x_large, y_large] = (riskmap[x, y] + x_r + y_r - 1) % 9 + 1
    return riskmap_enlarged


def main(input_path: Path):
    with input_path.open() as f:
        input_text = f.read()

    riskmap, Lx, Ly = parse(input_text)

    # ==== PART 1 ====
    print(lowest_risk(riskmap, Lx, Ly))

    # ==== PART 2 ====
    print(lowest_risk(enlarge(riskmap, Lx, Ly), 5 * Lx, 5 * Ly))
