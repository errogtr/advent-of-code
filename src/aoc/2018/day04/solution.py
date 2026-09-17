from collections import Counter, defaultdict
import re
import click
from aoc.utils import read_data, timer


def parse_logs(data):
    guard = None
    asleep = None
    schedule = defaultdict(Counter)
    for record in sorted(data.splitlines()):
        minute = int(record[15:17])
        if "shift" in record:
            guard = int(re.search(r"#(\d+)", record).group(1))
        elif "falls asleep" in record:
            asleep = minute
        else:  # "wakes up" in record
            for t in range(asleep, minute):
                schedule[guard][t] += 1
    return schedule


@timer
def part1(data):
    schedule = parse_logs(data)
    guard = max(schedule, key=lambda g: schedule[g].total())
    minute, _ = schedule[guard].most_common(1)[0]
    return guard * minute


@timer
def part2(data):
    schedule = parse_logs(data)

    mult = None
    sleep_count = 0
    for guard, minute_count in schedule.items():
        minute, count = minute_count.most_common(1)[0]
        if count > sleep_count:
            mult = minute * guard
            sleep_count = count

    return mult


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
