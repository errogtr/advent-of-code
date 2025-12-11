import re

import click
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

from aoc.utils import read_data, timer


def solve_min_sum_integer(M, b):
    M = np.array(M)
    b = np.array(b)
    m, n = M.shape

    # Objective: Minimize sum(a_i) -> coefficient vector is all 1s
    c = np.ones(n)

    # Constraints: M * a = b
    # Scipy requires lower and upper bounds for constraints.
    # For equality, lb == ub.
    constraints = LinearConstraint(M, lb=b, ub=b)

    # Bounds: a_i >= 0 (and technically < infinity)
    integrality = np.ones(n)  # 1 means integer constraint
    bounds = Bounds(lb=0, ub=np.inf)

    # Solve
    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

    return res.fun  # res.fun is the minimized sum


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
                next_lights = tuple(
                    1 - l if i in button else l for i, l in enumerate(curr_lights)
                )
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
    return int(min_presses)


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
        buttons_seq.append(
            [tuple(int(c) for c in b if c.isdigit()) for b in buttons_str.split()]
        )
        joltage_seq.append([int(c) for c in joltage_str.split(",") if c.isdigit()])

    # ==== PART 1 ====
    print(part1(lights_seq, buttons_seq))

    # ==== PART 2 ====
    print(part2(joltage_seq, buttons_seq))


if __name__ == "__main__":
    main()
