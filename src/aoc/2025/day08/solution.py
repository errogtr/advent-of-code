from collections import Counter
from itertools import combinations
from math import prod
import click

from aoc.utils import read_data, timer


def union(i, j, circuits):
    """Implements union part in union-find algorithm"""
    root_i = find(i, circuits)
    root_j = find(j, circuits)
    if root_i != root_j:
        circuits[root_j] = root_i
        return True
    return False


def find(i, circuits):
    """Implements find part in union-find algorithm"""
    if circuits[i] != i:
        circuits[i] = find(circuits[i], circuits)
    return circuits[i]


def dist(box_1, box_2):
    """Calculate squared Euclidean distance between two boxes."""
    return sum((x1 - x2) ** 2 for x1, x2 in zip(box_1, box_2))


@timer
def part1(n_boxes, distances, n_steps):
    circuits = list(range(n_boxes))

    for count in range(n_steps):
        _, i, j = distances[count]
        union(i, j, circuits)

    circuit_sizes = Counter(find(i, circuits) for i in range(n_boxes))
    return prod(size for _, size in circuit_sizes.most_common(3))


@timer
def part2(boxes, distances):
    n_circuits = len(boxes)
    circuits = list(range(n_circuits))

    for _, i, j in distances:
        was_merged = union(i, j, circuits)
        n_circuits -= was_merged

        if n_circuits == 1:
            return boxes[i][0] * boxes[j][0]


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    boxes = [[int(x) for x in box.split(",")] for box in data.splitlines()]

    # Compute all pairwise distances
    distances = []
    for (i, box_i), (j, box_j) in combinations(enumerate(boxes), 2):
        d = dist(box_i, box_j)
        distances.append((d, i, j))

    sorted_distances = sorted(distances)
    n_steps = 10 if example else 1000

    # ==== PART 1 ====
    print(part1(len(boxes), sorted_distances, n_steps))

    # ==== PART 2 ====
    print(part2(boxes, sorted_distances))


if __name__ == "__main__":
    main()
