from functools import cache
import click

from aoc.utils import read_data, timer


@timer
def part1(devices):
    def explore(curr):
        if curr == "out":
            return 1

        return sum(explore(device) for device in devices[curr])

    return explore("you")


@timer
def part2(devices):
    @cache
    def explore(curr, fft, dac):
        if curr == "out":
            return fft and dac

        count = 0
        for device in devices[curr]:
            fft = device == "fft" or fft
            dac = device == "dac" or dac
            count += explore(device, fft, dac)
        return count

    return explore("svr", False, False)


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    devices = {"out": list()}
    for line in data.splitlines():
        src, dst_list = line.split(": ")
        devices[src] = dst_list.split()

    # ==== PART 1 ====
    print(part1(devices))

    # ==== PART 2 ====
    print(part2(devices))


if __name__ == "__main__":
    main()
