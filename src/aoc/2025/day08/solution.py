from itertools import combinations
from math import prod
import click

from aoc.utils import read_data, timer


def dist(box_1, box_2):
    return sum((x1 - x2) ** 2 for x1, x2 in zip(box_1, box_2))


@timer
def part1(boxes, distances):
    circuits = list()
    for count in range(1000):
        _, i, j = distances[count]

        circuit_i, circuit_j = None, None
        for k, circuit in enumerate(circuits):
            if i in circuit:
                circuit_i = k
            if j in circuit:
                circuit_j = k

        if circuit_i is None and circuit_j is None:
            circuits.append({i, j})
        elif circuit_i is not None and circuit_j is None:
            circuits[circuit_i] |= {i, j}
        elif circuit_i is None and circuit_j is not None:
            circuits[circuit_j] |= {i, j}
        else:
            circuits[circuit_i] |= circuits[circuit_j]
            if circuit_i != circuit_j:
                circuits.pop(circuit_j)

        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            x_i, *_ = boxes[i]
            x_j, *_ = boxes[j]
            print(x_i * x_j)
            break

    return prod(sorted(len(c) for c in circuits)[-3:])


@timer
def part2(boxes, distances):
    circuits = list()
    for count in range(len(distances)):
        _, i, j = distances[count]

        circuit_i, circuit_j = None, None
        for k, circuit in enumerate(circuits):
            if i in circuit:
                circuit_i = k
            if j in circuit:
                circuit_j = k

        if circuit_i is None and circuit_j is None:
            circuits.append({i, j})
        elif circuit_i is not None and circuit_j is None:
            circuits[circuit_i] |= {i, j}
        elif circuit_i is None and circuit_j is not None:
            circuits[circuit_j] |= {i, j}
        else:
            circuits[circuit_i] |= circuits[circuit_j]
            if circuit_i != circuit_j:
                circuits.pop(circuit_j)

        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            x_i, *_ = boxes[i]
            x_j, *_ = boxes[j]
            return x_i * x_j


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    boxes = [[int(x) for x in box.split(",")] for box in data.splitlines()]
    distances = list()
    for (i, box_i), (j, box_j) in combinations(enumerate(boxes), 2):
        d = dist(box_i, box_j)
        distances.append((d, i, j))
    sorted_distances = sorted(distances)

    # ==== PART 1 ====
    print(part1(boxes, sorted_distances))

    # ==== PART 2 ====
    print(part2(boxes, sorted_distances))


if __name__ == "__main__":
    main()
