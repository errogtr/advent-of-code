from collections import deque
import re
import click
from aoc.utils import read_data, timer


INPUT_PATTERN = re.compile(r"(\d+) players; last marble is worth (\d+) points")


def game(players, marbles):
    scores = [0] * players
    circle = deque([0])
    for t in range(1, marbles + 1):
        if t % 23 == 0:
            circle.rotate(7)
            scores[t % players] += t + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(t)
    return max(scores)


@timer
def part1(data):
    players, marbles = map(int, INPUT_PATTERN.search(data).groups())
    return game(players, marbles)


@timer
def part2(data):
    players, marbles = map(int, INPUT_PATTERN.search(data).groups())
    return game(players, 100 * marbles)


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
