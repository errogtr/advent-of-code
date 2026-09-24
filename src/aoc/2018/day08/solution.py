from collections import defaultdict
import click
from aoc.utils import read_data, timer


def get_value(node, metadata, child_graph):
    children = child_graph[node]
    if children is None:
        return sum(metadata[node])
    
    value = 0
    for meta_idx in metadata[node]:
        if meta_idx - 1 < len(child_graph[node]):
            value += get_value(child_graph[node][meta_idx-1], metadata, child_graph)
    return value


@timer
def part1(data):
    numbers = [int(n) for n in data.split()]

    curr = 0
    nodes_stack = []
    metadata = 0
    to_process = {}
    is_header = True
    while curr < len(numbers):
        if is_header:
            children, meta_num = numbers[curr], numbers[curr+1]
            nodes_stack.append((curr, meta_num))
            to_process[curr] = children
            is_header = children != 0
            curr += 2
        else:
            _, meta_num = nodes_stack.pop()
            metadata += sum(numbers[curr:curr+meta_num])
            if nodes_stack:
                parent = nodes_stack[-1][0]
                to_process[parent] -= 1
                is_header = to_process[parent] != 0
            curr += meta_num
    return metadata


@timer
def part2(data):
    numbers = [int(n) for n in data.split()]

    curr = 0
    nodes_stack = []
    metadata = {}
    child_graph = defaultdict(list)
    to_process = {}
    is_header = True
    while curr < len(numbers):
        if is_header:
            children, meta_num = numbers[curr], numbers[curr+1]
            if children == 0:
                child_graph[curr] = None
            nodes_stack.append((curr, meta_num))
            to_process[curr] = children
            is_header = children != 0
            curr += 2
        else:
            node, meta_num = nodes_stack.pop()
            metadata[node] = numbers[curr:curr+meta_num]
            if nodes_stack:
                parent = nodes_stack[-1][0]
                to_process[parent] -= 1
                is_header = to_process[parent] != 0
                child_graph[parent].append(node)
            curr += meta_num
    
    return get_value(0, metadata, child_graph)


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

