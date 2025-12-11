from collections import defaultdict
from itertools import combinations, pairwise

import click
from tqdm import tqdm

from aoc.utils import read_data, timer


def area(p, q, r, s):
    return (r - p + 1) * (s - q + 1)


@timer
def part1(rectangles):
    return max(area(p, q, r, s) for p, q, r, s in rectangles)


@timer
def part2(coords, rectangles):
    perimeter = defaultdict(list)
    for (a, b), (c, d) in pairwise(coords + coords[:1]):
        if a == c:
            v_y = 1 if d > b else -1
            for t in range(min(b, d), max(b, d) + 1):
                perimeter[t].append((a, v_y))
    perimeter = {y: sorted(intervals) for y, intervals in perimeter.items()}

    max_area = 0
    for p, q, r, s in tqdm(rectangles):
        for y in range(q, s + 1):
            intervals = perimeter[y]
            outside = False
            if y == q or y == s:
                intersections = 0
                for left, turns in intervals:
                    if left > r:
                        break
                    intersections += turns
                if intersections == 0:
                    outside = True
            else:
                for x in [p, r]:
                    intersections = 0
                    for left, turn in intervals:
                        if x < left:
                            break
                        intersections += turn
                    if intersections == 0:
                        outside = True
                        break
            if outside:
                break
        else:
            max_area = max(max_area, area(p, q, r, s))

    return max_area


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    coords = [[int(x) for x in line.split(",")] for line in data.splitlines()]
    rectangles = list()
    for (a, b), (c, d) in combinations(coords, 2):
        p = min(a, c)
        q = min(b, d)
        r = max(a, c)
        s = max(b, d)
        rectangles.append((p, q, r, s))

    # ==== PART 1 ====
    print(part1(rectangles))

    # ==== PART 2 ====
    print(part2(coords, rectangles))


if __name__ == "__main__":
    main()
