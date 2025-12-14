import click
from aoc.utils import read_data, timer


@timer
def part1(policies):
    return sum(m <= pwd.count(c) <= M for m, M, c, pwd in policies)


@timer
def part2(policies):
    return sum((pwd[m - 1] == c) + (pwd[M - 1] == c) == 1 for m, M, c, pwd in policies)


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    policies = list()
    for line in data.splitlines():
        interval, char, pwd = line.split()
        hi, low = map(int, interval.split("-"))
        char = char.replace(":", "")
        policies.append((hi, low, char, pwd))

    # ==== PART 1 ====
    print(part1(policies))

    # ==== PART 2 ====
    print(part2(policies))


if __name__ == "__main__":
    main()
