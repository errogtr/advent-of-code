import click
from aoc.utils import read_data, timer


@timer
def part1(intervals, ids):
    fresh = 0
    for id in ids.splitlines():
        for left, right in intervals:
            if left <= int(id) <= right:
                fresh += 1
                break
    return fresh


@timer
def part2(intervals):
    merged_intervals = list()
    for left, right in sorted(intervals):
        if not merged_intervals:
            merged_intervals.append((left, right))
            continue

        prev_left, prev_right = merged_intervals[-1]
        if left <= prev_right:
            merged_intervals[-1] = (prev_left, max(right, prev_right))
        else:
            merged_intervals.append((left, right))

    return sum(right - left + 1 for left, right in merged_intervals)


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    id_ranges, ids = data.split("\n\n")
    intervals = list()
    for id_range in id_ranges.splitlines():
        left, right = map(int, id_range.split("-"))
        intervals.append((left, right))

    # ==== PART 1 ====
    print(part1(intervals, ids))

    # ==== PART 2 ====
    print(part2(intervals))


if __name__ == "__main__":
    main()
