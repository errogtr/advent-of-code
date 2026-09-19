from collections import defaultdict
import re

import click

from aoc.utils import read_data, timer


instr_pattern = re.compile(
    r"Step ([A-Z]) must be finished before step ([A-Z]) can begin."
)


def traverse(node, graph, executed):
    if node not in graph:
        node

    steps = sorted(graph[node])
    order = node
    for step in steps:
        executed[step][node] = True
        if all(executed[step].values()):
            order += traverse(step, graph, executed)
    return order


@timer
def part1(data):
    graph = defaultdict(list)
    executed = defaultdict(dict)
    nodes = set()
    for instruction in data.splitlines():
        step, next_step = instr_pattern.search(instruction).groups()
        graph[step].append(next_step)
        executed[next_step][step] = False
        nodes |= {step, next_step}

    order = ""
    stack = sorted(list(nodes - set(executed)))
    for node in stack:
        order += traverse(node, graph, executed)
    return order


@timer
def part2():
    pass


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2())


if __name__ == "__main__":
    main()
