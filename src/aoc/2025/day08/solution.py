from collections import Counter
from itertools import combinations
from math import prod
import click

from aoc.utils import read_data, timer


Box = list[int]
Dist = tuple[int, int, int]


def union(i: int, j: int, circuits: list[int]) -> bool:
    """Implements union part in union-find algorithm"""
    root_i = find(i, circuits)
    root_j = find(j, circuits)
    if root_i != root_j:
        circuits[root_j] = root_i
        return True
    return False


def find(i: int, circuits: list[int]) -> int:
    """Implements find part in union-find algorithm"""
    if circuits[i] != i:
        circuits[i] = find(circuits[i], circuits)
    return circuits[i]


def dist(box_i: Box, box_j: Box) -> int:
    """Calculate squared Euclidean distance between two boxes."""
    return sum((x_i - x_j) ** 2 for x_i, x_j in zip(box_i, box_j))


@timer
def part1(n_boxes: int, distances: list[Dist], n_steps: int) -> int:
    circuits = list(range(n_boxes))

    # Executing union-find only for N steps, i.e. first N sorted distances
    for _, i, j in distances[:n_steps]:
        union(i, j, circuits)

    circuit_sizes = Counter(find(i, circuits) for i in range(n_boxes))
    largest_three = sorted(circuit_sizes.values())[-3:]
    return prod(largest_three)


@timer
def part2(boxes: list[Box], distances: list[Dist]) -> int:
    n_circuits = len(boxes)
    circuits = list(range(n_circuits))

    t = 0
    while n_circuits > 1:
        _, i, j = distances[t]
        was_merged = union(i, j, circuits)
        n_circuits -= was_merged
        t += 1

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

    # Using different N steps based on whether we're executing the example or not
    n_steps = 10 if example else 1000

    # ==== PART 1 ====
    print(part1(len(boxes), sorted_distances, n_steps))

    # ==== PART 2 ====
    print(part2(boxes, sorted_distances))


if __name__ == "__main__":
    main()
