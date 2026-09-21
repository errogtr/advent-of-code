from collections import defaultdict
import re
from string import ascii_uppercase

import click

from aoc.utils import read_data, timer


instr_pattern = re.compile(
    r"Step ([A-Z]) must be finished before step ([A-Z]) can begin."
)


def build_graph(data, delay, with_time):
    graph = defaultdict(list)
    executed = defaultdict(dict)
    for instruction in data.splitlines():
        step, next_step = instr_pattern.search(instruction).groups()
        graph[step].append(next_step)
        executed[next_step][step] = delay + with_time * (ord(step) - 64)
    return graph, executed


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


@timer
def part1(data):
    graph, executed = build_graph(data, delay=1, with_time=False)

    order = ""
    for node in sorted(list(set(graph) - set(executed))):
        order += traverse(node, graph, executed)
    return order


@timer
def part2(data):
    graph, executed = build_graph(data, delay=60, with_time=True)
    counter = {c: 60 + ord(c) - 64 for c in ascii_uppercase}

    workers = [None, None, None, None,]
    queue = sorted(list(set(graph) - set(executed)))
    t = 0
    while True:
        for i, worker in enumerate(workers):
            if queue and worker is None:
                workers[i] = queue.pop(0)

        if all(w is None for w in workers):
            break

        for i, worker in enumerate(workers):
            if worker is None:
                continue

            counter[worker] = max(counter[worker] - 1, 0)
            if counter[worker] == 0:
                workers[i] = None

            buffer = []
            for node in sorted(graph[worker]):
                if all(counter[prev] == 0 for prev in executed[node]):
                    buffer.append(node)
                    
            queue = buffer + queue

        t += 1
        
        
    return t



@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2(data))


if __name__ == "__main__":
    main()
