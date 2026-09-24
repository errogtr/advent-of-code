import click
from aoc.utils import read_data, timer


def get_value(node):
    children, metadata = node
    if not children:
        return sum(metadata)

    value = 0
    for i in metadata:
        if 0 <= i - 1 < len(children):
            value += get_value(children[i - 1])
    return value


def parse_tree(data):
    """Needs to be iterative since for the given input a recursive solution hits the maximum recursion depth"""
    numbers = map(int, data.split())

    # [children to be read, metadata count, children list]
    stack = [[next(numbers), next(numbers), []]]
    root = None
    while stack:
        remaining, meta_count, children = stack[-1]
        if remaining > 0:
            stack[-1][0] -= 1
            stack.append([next(numbers), next(numbers), []])
        else:
            node = (children, [next(numbers) for _ in range(meta_count)])
            stack.pop()
            if stack:
                stack[-1][2].append(node)
            else:
                root = node
    return root


def sum_metadata(children, metadata):
    if not children:
        return sum(metadata)

    total = sum(metadata)
    for child in children:
        total += sum_metadata(*child)
    return total


@timer
def part1(data):
    tree = parse_tree(data)
    return sum_metadata(*tree)


@timer
def part2(data):
    tree = parse_tree(data)
    return get_value(tree)


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
