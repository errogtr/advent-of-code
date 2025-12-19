from collections import defaultdict
from heapq import heappop, heappush
from itertools import product

import click

from aoc.utils import read_data, timer


Coord = tuple[int, int]
MarkedPtLinks = dict[str, int]


def nearest_neighbors(x: int, y: int) -> list[Coord]:
    return [(x + vx, y + vy) for vx, vy in [(1, 0), (0, 1), (-1, 0), (0, -1)]]


def build_marked_pts_graph(
    marked_pts: dict[str, Coord], walls: set[Coord]
) -> dict[str, MarkedPtLinks]:
    marked_pts_graph: dict[str, MarkedPtLinks] = defaultdict(dict)
    for (start, start_pt), (end, end_pt) in product(marked_pts.items(), repeat=2):
        if start == end:
            continue

        queue = [(0, start_pt)]
        visited = {start_pt}
        while queue:
            curr_dist, curr_pt = heappop(queue)

            if curr_pt == end_pt:
                marked_pts_graph[start][end] = curr_dist
                break

            for next_pt in nearest_neighbors(*curr_pt):
                if next_pt not in visited and next_pt not in walls:
                    heappush(queue, (curr_dist + 1, next_pt))
                    visited.add(next_pt)

    return marked_pts_graph


@timer
def part1(marked_pts_graph: dict[str, MarkedPtLinks]) -> int:
    queue = [(0, frozenset({"0"}), "0")]
    target_size = len(marked_pts_graph)
    seen: set[tuple[str, frozenset[str]]] = set()

    while queue:
        curr_dist, visited, curr_location = heappop(queue)

        # Skip if we've seen this state before
        state = (curr_location, visited)
        if state in seen:
            continue
        seen.add(state)

        # Check if we've visited all marked points
        if len(visited) == target_size:
            return curr_dist

        # Explore neighbors
        for next_location, dist in marked_pts_graph[curr_location].items():
            if next_location not in visited:
                heappush(
                    queue, (curr_dist + dist, visited | {next_location}, next_location)
                )

    raise RuntimeError("No solution found.")


@timer
def part2(marked_pts_graph: dict[str, MarkedPtLinks]) -> int:
    min_dist: int | None = None
    queue = [(0, frozenset({"0"}), "0")]
    target_size = len(marked_pts_graph)
    seen: set[tuple[str, frozenset[str]]] = set()

    while queue:
        curr_dist, visited, curr_location = heappop(queue)

        # Skip if we've seen this state before
        state = (curr_location, visited)
        if state in seen:
            continue
        seen.add(state)

        # Prune paths that can't improve the best solution
        if min_dist is not None and curr_dist >= min_dist:
            continue

        # Check if we've visited all marked points
        if len(visited) == target_size:
            dist_to_zero = marked_pts_graph[curr_location]["0"]
            full_length = curr_dist + dist_to_zero
            min_dist = full_length if min_dist is None else min(min_dist, full_length)
            continue

        # Explore neighbors
        for next_location, dist in marked_pts_graph[curr_location].items():
            if next_location not in visited:
                heappush(
                    queue, (curr_dist + dist, visited | {next_location}, next_location)
                )

    if min_dist is None:
        raise RuntimeError("No solution found.")

    return min_dist


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    walls = set()
    marked_pts = dict()
    for y, row in enumerate(data.splitlines()):
        for x, val in enumerate(row):
            if val in "0123456789":
                marked_pts[val] = (x, y)
            elif val == "#":
                walls.add((x, y))

    marked_pts_graph = build_marked_pts_graph(marked_pts, walls)

    # ==== PART 1 ====
    print(part1(marked_pts_graph))

    # ==== PART 2 ====
    print(part2(marked_pts_graph))


if __name__ == "__main__":
    main()
