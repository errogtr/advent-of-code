from collections import defaultdict
from pathlib import Path


def find_group(start, pipes):
    visited = {start}
    queue = [start]
    while queue:
        curr = queue.pop()
        for next in pipes[curr]:
            if next not in visited:
                queue.append(next)
                visited.add(next)
    return visited


def main(input_path: Path):
    with input_path.open() as f:
        data = f.read()

    pipes = defaultdict(list)
    for line in data.splitlines():
        node, links = line.split(" <-> ")
        pipes[node] = links.split(", ")

    # ==== PART 1 ====
    print(len(find_group('0', pipes)))

    # ==== PART 2 ====
    starts = set(pipes)
    groups = 0
    while starts:
        starts -= find_group(starts.pop(), pipes)
        groups += 1
    print(groups)
    
