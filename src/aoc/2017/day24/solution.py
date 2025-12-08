from collections import defaultdict
import click

from aoc.utils import read_data, timer


@timer
def part1(connections):
    def bridge(port, used_pin, visited):
        pin_1, pin_2 = port
        strength = pin_1 + pin_2

        free_pin = pin_1 if used_pin == pin_2 else pin_2
        next_ports = connections[free_pin] - visited

        if not next_ports:
            return strength

        return max(strength + bridge(p, free_pin, visited | {p}) for p in next_ports)

    return max(bridge(port, 0, {port}) for port in connections[0])


@timer
def part2():
    pass


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    connections = defaultdict(set)
    for port in data.splitlines():
        pin_1, pin_2 = map(int, port.split("/"))
        connections[pin_1].add((pin_1, pin_2))
        connections[pin_2].add((pin_1, pin_2))

    # ==== PART 1 ====
    print(part1(connections))

    # ==== PART 2 ====
    print(part2(connections))


if __name__ == "__main__":
    main()
