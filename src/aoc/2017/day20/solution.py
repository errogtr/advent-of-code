from collections import defaultdict
from itertools import combinations
from math import floor, sqrt
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


def solve(a, b, c):
    """
    Solves (t * (t + 1)) // 2 * a + t * b + c = 0 for integer positive t
    """
    if a == 0:
        if b == 0 or c % b != 0:
            return None
        return -c // b
    else:
        A = 2 * a
        B = a + 2 * b
        D = B**2 - 4 * A * c
        if D < 0:
            return None
        s = floor(sqrt(D))
        if s * s != D:
            return None

        # looking for min positive t-solution
        t_candidates = list()
        if (-B - s) % A == 0:
            t_candidates.append((-B - s) // A)
        if (-B + s) % A == 0:
            t_candidates.append((-B + s) // A)
        t_positive = [t for t in t_candidates if t >= 0]
        if t_positive:
            return min(t_positive)

    return None


@timer
def part1(particles):
    magnitudes = [(manhattan(a), manhattan(v), manhattan(p)) for p, v, a in particles]
    slow = min(range(len(particles)), key=lambda i: magnitudes[i])
    return slow


@timer
def part2(particles):
    collisions = defaultdict(set)
    for (id_1, ptcl_1), (id_2, ptcl_2) in combinations(enumerate(particles), 2):
        p_1, v_1, a_1 = ptcl_1
        p_2, v_2, a_2 = ptcl_2

        x_1, y_1, z_1 = p_1
        vx_1, vy_1, vz_1 = v_1
        ax_1, ay_1, az_1 = a_1

        x_2, y_2, z_2 = p_2
        vx_2, vy_2, vz_2 = v_2
        ax_2, ay_2, az_2 = a_2

        ax_delta = ax_2 - ax_1
        ay_delta = ay_2 - ay_1
        az_delta = az_2 - az_1

        vx_delta = vx_2 - vx_1
        vy_delta = vy_2 - vy_1
        vz_delta = vz_2 - vz_1

        px_delta = x_2 - x_1
        py_delta = y_2 - y_1
        pz_delta = z_2 - z_1

        # find integer collision time in the future for x axis
        # if the same t_coll solves the quadratic equation
        #
        #   (t * (t + 1)) // 2 * a + t * b + c = 0
        #
        #          |- a = a*2 - a*1
        #   where: |- b = v*2 - v*1
        #          |- c = p*2 - p*1
        #
        #  then p*1(t_coll) = p*2(coll_)
        #
        if (t_coll := solve(ax_delta, vx_delta, px_delta)) is not None:
            y_delta_t_coll = evolve(t_coll, ay_delta, vy_delta, py_delta)
            z_delta_t_coll = evolve(t_coll, az_delta, vz_delta, pz_delta)
            if y_delta_t_coll == 0 and z_delta_t_coll == 0:
                collisions[t_coll] |= {id_1, id_2}

    # remove particle ids with respect to time ordering of collisions
    particle_ids = set(range(len(particles)))
    for t in sorted(collisions):
        particle_ids -= collisions[t]

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
