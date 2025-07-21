from pathlib import Path

from ..day10.solution import knot_hash


def hex2bin(c):
    return f"{int(c, 16):04b}"


def bin_row(row_key):
    return "".join(hex2bin(c) for c in knot_hash(row_key))


def nesw(x, y):
    N = x, y - 1
    E = x + 1, y
    S = x, y + 1
    W = x - 1, y
    return (N, E, S, W)


def get_nn(k, L):
    x, y = k % L, k // L
    return [w * L + z for z, w in nesw(x, y) if 0 <= z < L and 0 <= w < L]


def main(input_path: Path):
    with input_path.open() as f:
        key_string = f.read()

    L = 128
    grid = "".join(bin_row(f"{key_string}-{i}") for i in range(L))

    # ==== PART 1 ====
    print(grid.count("1"))

    # ==== PART 2 ====
    regions = 0
    visited = set()
    for k, val in enumerate(grid):
        if val == "0" or k in visited:
            continue

        visited.add(k)
        queue = [k]
        while queue:
            curr = queue.pop()
            for nn in get_nn(curr, L):
                if grid[nn] == "1" and nn not in visited:
                    queue.append(nn)
                    visited.add(nn)
        regions += 1

    print(regions)
