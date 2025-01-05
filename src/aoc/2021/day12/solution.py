from collections import Counter, defaultdict
from copy import copy
from pathlib import Path


START = "start"
END = "end"


def parse(links: list[str]) -> dict[str, list[str]]:
    caves = defaultdict(list)
    for link in links:
        x, y = link.split("-")
        if y != START:
            caves[x].append(y)
        if x != START:
            caves[y].append(x)
    return caves


def visit(curr_cave: str, caves: dict, visits_count: Counter, max_visits: int) -> int:
    if curr_cave == END:
        return 1

    paths = 0
    if curr_cave.islower():
        visits_count[curr_cave] += 1

    for next_cave in caves[curr_cave]:
        if not (visits_count[next_cave] > 0 and max_visits in visits_count.values()):
            paths += visit(next_cave, caves, copy(visits_count), max_visits)
    return paths


def main(input_path: Path):
    with input_path.open() as f:
        links = f.read().splitlines()

    caves = parse(links)

    # ==== PART 1 ====
    print(visit(START, caves, Counter(), 1))

    # ==== PART 2 ====
    print(visit(START, caves, Counter(), 2))
