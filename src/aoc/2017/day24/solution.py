from collections import defaultdict
import click

from aoc.utils import read_data, timer


@timer
def part1(connections):
    def bridge(p1, p2, used_pin, visited):
        free_pin = p1 if used_pin == p2 else p2
        next_ports = connections[free_pin] - visited

        if not next_ports:
            return p1 + p2

        return p1 + p2 + max(bridge(*p, free_pin, visited | {p}) for p in next_ports)

    return max(bridge(*port, 0, {port}) for port in connections[0])


@timer
def part2(connections):
    def bridge(p1, p2, used_pin, length, visited):
        free_pin = p1 if used_pin == p2 else p2
        next_ports = connections[free_pin] - visited

        if not next_ports:
            return length, p1 + p2

        max_len_str = (0, 0)
        for p in next_ports:
            sub_len, sub_str = bridge(*p, free_pin, length + 1, visited | {p})
            max_len_str = max(max_len_str, (sub_len, p1 + p2 + sub_str))
        return max_len_str

    max_len, best_str = max(bridge(*port, 0, 1, {port}) for port in connections[0])
    return best_str


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
