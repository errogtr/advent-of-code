from collections import defaultdict
import re
from string import ascii_uppercase

import click

from aoc.utils import read_data, timer


INSTR_PATTERN = re.compile(
    r"Step ([A-Z]) must be finished before step ([A-Z]) can begin."
)


def traverse(node, graph, executed):
    if node not in graph:
        node

    steps = sorted(graph[node])
    order = node
    for step in steps:
        executed[step][node] -= 1
        if all(t == 0 for t in executed[step].values()):
            order += traverse(step, graph, executed)
    return order


def parse_dependencies(data):
    dependencies = defaultdict(set)
    steps = set()
    for line in data.splitlines():
        prereq, step = INSTR_PATTERN.search(line).groups()
        dependencies[step].add(prereq)
        steps.update((prereq, step))

    # Steps with no prerequisites still need an entry.
    for step in steps:
        dependencies.setdefault(step, set())
    return dependencies


def step_duration(step, base_delay):
    return base_delay + (ord(step) - ord("A") + 1)


@timer
def part1(data):
    remaining = parse_dependencies(data)
    order = []

    while remaining:
        ready = sorted(step for step, deps in remaining.items() if deps <= set(order))
        next_step = ready[0]
        order.append(next_step)
        del remaining[next_step]

    return "".join(order)


@timer
def part2(data, num_workers, base_delay):
    remaining = parse_dependencies(data)
    done = set()
    in_progress = {}
    free_workers = num_workers

    t = 0
    while remaining or in_progress:
        ready = sorted(step for step, deps in remaining.items() if deps <= done)
        for step in ready:
            if free_workers == 0:
                break
            in_progress[step] = step_duration(step, base_delay)
            del remaining[step]
            free_workers -= 1

        for step in list(in_progress):
            in_progress[step] -= 1
            if in_progress[step] == 0:
                done.add(step)
                del in_progress[step]
                free_workers += 1

        t += 1
    return t


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2(data, num_workers=2 if example else 5, base_delay=0 if example else 60))


if __name__ == "__main__":
    main()
