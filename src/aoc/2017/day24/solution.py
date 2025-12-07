from collections import defaultdict
import click

from aoc.utils import read_data, timer


def bridge(port, target_ports, occupied, visited):
    pins = port.split("/")
    strength = sum(map(int, pins))
    next_ports = list()
    for target_port in target_ports:
        if target_port in visited:
            continue
        pin_1, pin_2 = target_port.split("/")
        if pin_1 in pins:
            next_ports.append(target_port)
        elif pin_2 in pins:
            next_ports.append(target_port)

    if not target_ports:
        return strength


@timer
def part1(data):
    ports = sorted(data.splitlines())

    zero_pin_ports = list()
    target_ports = list()
    for port in ports:
        if port.startswith("0"):
            zero_pin_ports.append(port)
        else:
            target_ports.append(port)

    brigdes = defaultdict(dict)
    for init_port in zero_pin_ports:
        strength = bridge(init_port, target_ports, "0", {init_port})



@timer
def part2():
    pass


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2())


if __name__ == "__main__":
    main()
