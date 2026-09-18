from itertools import product
import click
from aoc.utils import read_data, timer


Coords = tuple[int, int]


def get_coordinates(data) -> tuple[list[Coords], int, int]: 
    coordinates = list()
    max_x, max_y = 0, 0
    for coords_raw in data.splitlines():
        x, y = map(int, coords_raw.split(","))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        coordinates.append((x, y))
    return coordinates, max_x, max_y


@timer
def part1(data):
    coordinates, max_x, max_y = get_coordinates(data)
    closest = [set() for _ in range(len(coordinates))]
    for x, y in product(range(max_x+1), range(max_y+1)):
        distances = list()

        for X, Y in coordinates:
            distances.append(abs(x - X) + abs(y - Y))

        min_distance = min(distances)
        if distances.count(min_distance) == 1:
            closest[distances.index(min_distance)].add((x, y))

    largest_finite_area = 0
    for region in closest:
        for (x, y) in region:
            if x == 0 or y == 0 or x == max_x or y == max_y:
                break
        else:
            largest_finite_area = max(largest_finite_area, len(region))

    return largest_finite_area


@timer
def part2(data, max_dist):
    coordinates, max_x, max_y = get_coordinates(data)

    region = 0
    for x, y in product(range(max_x+1), range(max_y+1)):
        if sum(abs(x - X) + abs(y - Y) for X, Y in coordinates) < max_dist:
            region += 1
    
    return region


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    max_dist = 32 if example else 10_000
    print(part2(data, max_dist=max_dist))


if __name__ == "__main__":
    main()

