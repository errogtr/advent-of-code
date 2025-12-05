import click
from aoc.utils import read_data, timer


@timer
def part1(intervals, ids):
    fresh = 0
    for id in ids.splitlines():
        for l, r in intervals:
            if l <= int(id) <= r:
                fresh += 1
                break
    return fresh


@timer
def part2(intervals):
    merged_intervals = list()
    for l, r in sorted(intervals):
        if not merged_intervals:
            merged_intervals.append((l, r))
            continue

        prev_l, prev_r = merged_intervals[-1]
        if l <= prev_r:
            merged_intervals[-1] = (prev_l, max(r, prev_r))
        else:
            merged_intervals.append((l, r))

    return sum(r - l + 1 for l, r in merged_intervals)


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    id_ranges, ids = data.split("\n\n")
    intervals = list()
    for id_range in id_ranges.splitlines():
        l, r = map(int, id_range.split("-"))
        intervals.append((l, r))

    # ==== PART 1 ====
    print(part1(intervals, ids))

    # ==== PART 2 ====
    print(part2(intervals))


if __name__ == "__main__":
    main()
