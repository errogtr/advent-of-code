from collections import defaultdict
from itertools import combinations, pairwise

import click
from tqdm import tqdm

from aoc.utils import read_data, timer


def area(a, b, c, d):
    """One corner is (a, b), the other is (c, d)"""
    return (abs(a - c) + 1) * (abs(b - d) + 1)


def triplewise(seq):
    return zip(seq, seq[1:], seq[2:])


@timer
def part1(coords):
    return max(area(a, b, c, d) for (a, b), (c, d) in combinations(coords, 2))


@timer
def part2(coords):
    perimeter = defaultdict(list)
    min_x = 0
    for (a, b), (c, d) in pairwise(coords + coords[:1]):
        x = min(a, c)
        y = min(b, d)
        z = max(a, c)
        w = max(b, d)
        if y == w:
            # turn = 1 if f > w else -1
            # perimeter[y].append((x, z, turn))
            pass
        else:
            v_y = 1 if d > b else -1
            for t in range(y, w + 1):
                perimeter[t].append((x, z, v_y))
        min_x = min(x, min_x)
    perimeter = {y: sorted(intervals) for y, intervals in perimeter.items()}

    max_area = 0
    comb = len(coords) * (len(coords) - 1) // 2
    for (a, b), (c, d) in tqdm(combinations(coords, 2), total=comb):
        p = min(a, c)
        q = min(b, d)
        r = max(a, c)
        s = max(b, d)

        for y in range(q, s + 1):
            intervals = perimeter[y]
            outside = False
            if y == q or y == s:
                intersections = 0
                for left, right, turns in intervals:
                    if right < p:
                        continue
                    if left > r:
                        break
                    intersections += turns
                if intersections == 0:
                    outside = True
            else:
                for x in [p, r]:
                    intersections = 0
                    for left, right, turn in intervals:
                        if x < left:
                            break
                        intersections += turn
                    if intersections == 0:
                        outside = True
                        break
            if outside:
                break

        if not outside:
            max_area = max(max_area, area(a, b, c, d))

    return max_area


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    coords = [[int(x) for x in line.split(",")] for line in data.splitlines()]

    # ==== PART 1 ====
    print(part1(coords))

    # ==== PART 2 ====
    print(part2(coords))


if __name__ == "__main__":
    main()
