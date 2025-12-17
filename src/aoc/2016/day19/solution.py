from math import floor, log
import click
from aoc.utils import read_data, timer


@timer
def part1(data: str) -> int:
    """Write any number N as 2^n + k, where n is the largest integer
    s.t. 2^n < N, and 0 <= k < 2^n.
    Then: f(2^n + k) = 2k + 1"""
    N = int(data)
    return 2 * (N - 2 ** floor(log(N, 2))) + 1


@timer
def part2(data: str) -> int:
    """Write any number N as 3^n + k, where n is the largest integer
    s.t. 3^n < N, and 1 <= k < 2 * 3^n.

                        |- k,          if 1 <= k < 3^n
    Then: f(3^n + k) = -|
                        |- 2k - 3^n,   if 3^n <= k < 2*3^n
    """

    N = int(data)
    pow3 = 3 ** floor(log(N, 3))
    return k if 1 <= (k := (N - pow3)) < pow3 else 2 * k - pow3


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
