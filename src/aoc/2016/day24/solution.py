from collections import defaultdict
from heapq import heappop, heappush
from itertools import product
from math import inf
import click
from aoc.utils import read_data, timer


Coord = tuple[int, int]

def nearest_neighbors(x: int, y: int) -> list[Coord]:
    return [(x + vx, y + vy) for vx, vy in [(1, 0), (0, 1), (-1, 0), (0, -1)]]


@timer
def part1(ducts: dict[Coord, str], marked_pts: dict[str, Coord]) -> int:
    # floodfill to get marked points graph (relevant locations + crossings)
    marked_pts_graph = defaultdict(list)
    for (start, start_pt), (end, end_pt) in product(marked_pts.items(), repeat=2):
        if start == end:
            continue

        queue = [(0, start_pt)]
        visited = {start_pt}
        while queue:
            curr_dist, curr_pt = heappop(queue)
            
            if curr_pt == end_pt:
                marked_pts_graph[start].append((end, curr_dist))
                break

            for next_pt in nearest_neighbors(*curr_pt):
                if next_pt not in visited and ducts[next_pt] != "#":
                    heappush(queue, (curr_dist + 1, next_pt))
                    visited.add(next_pt)

    curr_dist = 0
    curr_path = "0"
    curr_location = "0"
    queue = [(curr_dist, curr_path, curr_location)]
    while queue:
        curr_dist, curr_path, curr_location = heappop(queue)

        if len(curr_path) == len(marked_pts):
            break

        for next_location, dist in marked_pts_graph[curr_location]:
            if next_location not in curr_path:
                next_path = curr_path + next_location
                heappush(queue, (curr_dist + dist, next_path, next_location))
    
    return curr_dist


@timer
def part2(ducts: dict[Coord, str], marked_pts: dict[str, Coord]) -> int:
    # floodfill to get marked points graph (relevant locations + crossings)
    marked_pts_graph = defaultdict(dict)
    for (start, start_pt), (end, end_pt) in product(marked_pts.items(), repeat=2):
        if start == end:
            continue

        queue = [(0, start_pt)]
        visited = {start_pt}
        while queue:
            curr_dist, curr_pt = heappop(queue)
            
            if curr_pt == end_pt:
                marked_pts_graph[start] |= {end: curr_dist}
                break

            for next_pt in nearest_neighbors(*curr_pt):
                if next_pt not in visited and ducts[next_pt] != "#":
                    heappush(queue, (curr_dist + 1, next_pt))
                    visited.add(next_pt)

    min_dist = inf
    curr_dist = 0
    curr_path = "0"
    curr_location = "0"
    queue = [(curr_dist, curr_path, curr_location)]
    while queue:
        curr_dist, curr_path, curr_location = heappop(queue)

        if set(curr_path) == set(marked_pts):
            dist_to_zero = marked_pts_graph[curr_location]["0"]
            min_dist = min(min_dist, curr_dist + dist_to_zero)

        for next_location, dist in marked_pts_graph[curr_location].items():
            if next_location not in curr_path:
                next_path = curr_path + next_location
                heappush(queue, (curr_dist + dist, next_path, next_location))
    
    return min_dist


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)
    
    ducts = dict()
    marked_pts = dict()
    for y, row in enumerate(data.splitlines()):
        for x, val in enumerate(row):
            ducts[(x, y)] = val
            if val in "0123456789":
                marked_pts[val] = (x, y)

    # ==== PART 1 ====
    print(part1(ducts, marked_pts))

    # ==== PART 2 ====
    print(part2(ducts, marked_pts))


if __name__ == "__main__":
    main()
