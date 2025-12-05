from collections import defaultdict
from itertools import combinations
from math import floor, inf, sqrt
import re

import click

from aoc.utils import read_data, timer


COMPONENTS = re.compile(r"(-*\d+),(-*\d+),(-*\d+)")


def parse(line):
    p, v, a = line.split(", ")
    p = tuple(map(int, COMPONENTS.search(p).groups()))
    v = tuple(map(int, COMPONENTS.search(v).groups()))
    a = tuple(map(int, COMPONENTS.search(a).groups()))
    return p, v, a


def manhattan(x) -> int:
    return sum(map(abs, x))


def evolve(t, a, b, c):
    return (t * (t + 1)) // 2 * a + t * b + c


@timer
def part1(particles):
    magnitudes = [(manhattan(a), manhattan(v), manhattan(p)) for p, v, a in particles]
    slow = min(range(len(particles)), key=lambda i: magnitudes[i])
    return slow


@timer
def part2(particles):
    collisions = defaultdict(set)
    for (id_alpha, alpha), (id_beta, beta) in combinations(enumerate(particles), 2):
        p_alpha, v_alpha, a_alpha = alpha
        p_beta, v_beta, a_beta = beta

        x_alpha, y_alpha, z_alpha = p_alpha
        vx_alpha, vy_alpha, vz_alpha = v_alpha
        ax_alpha, ay_alpha, az_alpha = a_alpha

        x_beta, y_beta, z_beta = p_beta
        vx_beta, vy_beta, vz_beta = v_beta
        ax_beta, ay_beta, az_beta = a_beta

        ax = ax_beta - ax_alpha
        ay = ay_beta - ay_alpha
        az = az_beta - az_alpha

        bx = vx_beta - vx_alpha
        by = vy_beta - vy_alpha
        bz = vz_beta - vz_alpha

        cx = x_beta - x_alpha
        cy = y_beta - y_alpha
        cz = z_beta - z_alpha

        # find integer collision time in the future for x axis
        if ax == 0:
            if bx == 0 or cx % bx != 0:
                continue
            t_coll = -cx // bx
        else:
            A = 2 * ax
            B = (ax + 2 * bx)
            D = B ** 2 - 4 * A * cx
            if D < 0:
                continue
            s = floor(sqrt(D))
            if s * s != D:
                continue

            t_1, t_2 = -inf, -inf
            if (-B - s) % A == 0:
                t_1 = (-B - s) // A
            if (-B + s) % A == 0:
                t_2 = (-B + s) // A

            t_min = min(t_1, t_2)
            t_max = max(t_1, t_2)
            # both collisions in the future
            if t_min >= 0:  
                t_coll = t_min
            # one collision in the past and one in the future
            elif t_max >= 0:  
                t_coll = t_max
            # both collisions in the past
            else:  
                continue

        y_delta_t_coll = evolve(t_coll, ay, by, cy)
        z_delta_t_coll = evolve(t_coll, az, bz, cz)
        if y_delta_t_coll == 0 and z_delta_t_coll == 0:
            collisions[t_coll] |= {id_alpha, id_beta}

    particle_ids = set(range(len(particles)))
    for t in sorted(collisions):
        for id in collisions[t]:
            if id in particle_ids:
                particle_ids.remove(id)

    return len(particle_ids)


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    particles = [parse(line) for line in data.splitlines()]

    # ==== PART 1 ====
    print(part1(particles))

    # ==== PART 2 ====
    print(part2(particles))


if __name__ == "__main__":
    main()
