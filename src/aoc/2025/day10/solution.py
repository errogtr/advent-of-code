from fractions import Fraction
from itertools import product
import re

import click
from tqdm import tqdm
from aoc.utils import read_data, timer


def solve_min_sum_integer(M, b):
    """
    Solve:
        minimize sum(a_i)
        subject to M * a = b
        a_i >= 0, integer

    M: list of lists (m x n)
    b: list (m)
    """

    # Convert to Fractions
    M = [[Fraction(x) for x in row] for row in M]
    b = [Fraction(x) for x in b]
    m = len(M)
    n = len(M[0])

    # --- Step 1: Row-reduce to find solution space ---
    # Augment matrix
    A = [row + [b[i]] for i, row in enumerate(M)]

    # Gaussian elimination
    r = 0
    pivots = []
    for c in range(n):
        # find pivot
        pivot = None
        for i in range(r, m):
            if A[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue

        A[r], A[pivot] = A[pivot], A[r]
        pivots.append(c)

        # normalize row
        fac = A[r][c]
        A[r] = [x / fac for x in A[r]]

        # eliminate
        for i in range(m):
            if i != r and A[i][c] != 0:
                fac = A[i][c]
                A[i] = [A[i][j] - fac * A[r][j] for j in range(n+1)]
        r += 1

    # Check for inconsistency
    for row in A:
        if all(col == 0 for col in row[:-1]) and row[-1] != 0:
            return []  # no solution

    # --- Step 2: Build particular solution + nullspace ---
    free_vars = [j for j in range(n) if j not in pivots]

    # Particular solution (set free vars = 0)
    a0 = [Fraction(0)] * n
    for i, c in enumerate(pivots):
        a0[c] = A[i][n]

    # Nullspace basis vectors
    nullvecs = []
    for free in free_vars:
        v = [Fraction(0)] * n
        v[free] = 1
        # Solve for pivot variables
        for i, c in enumerate(pivots):
            v[c] = -A[i][free]
        nullvecs.append(v)

    # --- Step 3: Search integer combinations of nullspace ---
    # Bound free integer parameters using non-negativity
    # We use small search windows for safety: expand if needed
    search_range = range(0, 200)
    best_val = None
    for params in tqdm(product(search_range, repeat=len(nullvecs))):
        # build solution a = a0 + sum(params[k] * nullvecs[k])
        a = a0[:]
        for k, t in enumerate(params):
            for i in range(n):
                a[i] += t * nullvecs[k][i]

        # check integer and non-negative
        if any(x < 0 for x in a):
            continue
        if any(x.denominator != 1 for x in a):
            continue

        a_int = [int(x) for x in a]
        s = sum(a_int)

        if best_val is None or s < best_val:
            best_val = s

    return best_val


@timer
def part1(lights_seq, buttons_seq):
    min_presses = 0
    for lights, buttons in zip(lights_seq, buttons_seq):
        start = (0,) * len(lights)
        queue = [(0, start)]
        visited = {start}
        while queue:
            presses, curr_lights = queue.pop(0)

            if curr_lights == lights:
                min_presses += presses
                break

            for button in buttons:
                next_lights = tuple(1 - l if i in button else l for i, l in enumerate(curr_lights))
                if next_lights not in visited:
                    queue.append((presses + 1, next_lights))
                    visited.add(next_lights)
            
    return min_presses


@timer
def part2(joltage_seq, buttons_seq):
    min_presses = 0
    for target_joltage, buttons in zip(joltage_seq, buttons_seq):
        M = [[0] * len(buttons) for _ in range(len(target_joltage))]
        for j, button in enumerate(buttons):
            for i in button:
                M[i][j] = 1
        min_presses += solve_min_sum_integer(M, target_joltage)
    return min_presses


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    lights_seq, buttons_seq, joltage_seq = list(), list(), list()
    for line in data.splitlines():
        lights_str = re.search(r"\[(.+)\]", line).group(1)
        buttons_str = re.search(r"(\(.+\))", line).group(1)
        joltage_str = re.search(r"\{(.+)\}", line).group(1)
        
        lights_seq.append(tuple(1 if light == "#" else 0 for light in lights_str))
        buttons_seq.append([tuple(int(c) for c in b if c.isdigit()) for b in buttons_str.split()])
        joltage_seq.append([int(c) for c in joltage_str.split(",") if c.isdigit()])

    # ==== PART 1 ====
    print(part1(lights_seq, buttons_seq))

    # ==== PART 2 ====
    print(part2(joltage_seq, buttons_seq))


if __name__ == "__main__":
    main()
