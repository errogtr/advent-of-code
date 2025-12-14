from collections import defaultdict
from itertools import combinations, pairwise

import click

from aoc.utils import read_data, timer


def area(rect):
    """Calculate area of rectangle (p, q, r, s) where (p,q) is top-left, (r,s) is bottom-right."""
    p, q, r, s = rect
    return (r - p + 1) * (s - q + 1)


def build_interval_map(coords):
    """
    Build interval map for efficient ray casting.
    For each y-coordinate, we track which x-ranges are inside the polygon.
    Also identify critical y-coordinates where horizontal edges exist.

    Returns:
        - interval_map: dict mapping y -> sorted list of (x, delta_winding) events
        - critical_y: sorted set of y-coordinates where horizontal edges exist
    """
    events = defaultdict(list)  # y -> list of (x, delta_winding)
    critical_y = set()

    for (x1, y1), (x2, y2) in pairwise(coords + coords[:1]):
        if x1 == x2:  # Vertical edge
            orientation = 1 if y2 > y1 else -1
            y_min, y_max = min(y1, y2), max(y1, y2)

            for y in range(y_min, y_max + 1):
                events[y].append((x1, orientation))
        else:  # Horizontal edge
            # Mark the y-coordinates where horizontal edges exist
            critical_y.add(y1)
            critical_y.add(y2)

    # Sort events by x-coordinate for each y
    interval_map = {y: sorted(edge_list) for y, edge_list in events.items()}

    return interval_map, sorted(critical_y)


def is_range_inside(x_start, x_end, y, interval_map):
    """
    Check if the entire range [x_start, x_end] at height y is inside the polygon.
    Uses winding number: we check at x_start and x_end, and verify no edges cross in between.
    """
    if y not in interval_map:
        return False

    events = interval_map[y]

    # Calculate winding at x_start
    winding_start = 0
    for edge_x, delta in events:
        if edge_x > x_start:
            break
        if edge_x <= x_start:
            winding_start += delta

    # If start point is outside, range is outside
    if winding_start == 0:
        return False

    # Check if any edges cross our range (x_start, x_end)
    # If an edge is strictly between x_start and x_end, the winding changes
    for edge_x, delta in events:
        if edge_x <= x_start:
            continue
        if edge_x >= x_end:
            break
        # There's an edge strictly inside our range
        # Check if winding stays non-zero
        winding_start += delta
        if winding_start == 0:
            return False

    # Calculate winding at x_end
    winding_end = 0
    for edge_x, delta in events:
        if edge_x > x_end:
            break
        winding_end += delta

    return winding_end != 0


def get_y_segments(q, s, critical_y):
    """
    Divide the y-range [q, s] into segments based on critical y-coordinates.
    Returns list of (y_start, y_end) tuples representing contiguous segments
    where no horizontal edges cross.
    """
    # Find critical y values within our range
    relevant_critical = [y for y in critical_y if q <= y <= s]

    if not relevant_critical:
        # No critical points in range, entire range is one segment
        return [(q, s)]

    segments = []
    current = q

    for critical in relevant_critical:
        if current < critical:
            # Segment before the critical point
            segments.append((current, critical - 1))
        # The critical point itself
        segments.append((critical, critical))
        current = critical + 1

    # Segment after the last critical point
    if current <= s:
        segments.append((current, s))

    return segments


def is_rect_inside(rect, interval_map, critical_y):
    """
    Check if rectangle is inside polygon using interval-based checking.
    Optimized to only check representative y-levels in each segment.
    """
    p, q, r, s = rect

    # Divide y-range into segments where topology doesn't change
    y_segments = get_y_segments(q, s, critical_y)

    for y_start, y_end in y_segments:
        # Only need to check one representative y in this segment
        # Check the first one
        if not is_range_inside(p, r, y_start, interval_map):
            return False

        # If segment has multiple y-values, check the last one too
        # (in case there's a boundary condition)
        if y_end > y_start:
            if not is_range_inside(p, r, y_end, interval_map):
                return False

    return True


@timer
def part1(rectangles):
    """Find maximum area rectangle using any two corner points."""
    return max(area(rect) for rect in rectangles)


@timer
def part2(coords, rectangles):
    """Find maximum area rectangle that fits entirely inside the polygon."""
    interval_map, critical_y = build_interval_map(coords)
    max_area = 0

    # Process rectangles from largest to smallest for early termination
    for rect in sorted(rectangles, key=area, reverse=True):
        curr_area = area(rect)

        # Early termination: can't beat current max
        if curr_area <= max_area:
            break

        # Check if rectangle fits inside polygon
        if is_rect_inside(rect, interval_map, critical_y):
            max_area = curr_area

    return max_area


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    # Parse polygon vertices
    coords = [[int(x) for x in line.split(",")] for line in data.splitlines()]

    # Generate all possible rectangles from pairs of corner points
    rectangles = []
    for (a, b), (c, d) in combinations(coords, 2):
        p, q = min(a, c), min(b, d)
        r, s = max(a, c), max(b, d)
        rectangles.append((p, q, r, s))

    # ==== PART 1 ====
    print(part1(rectangles))

    # ==== PART 2 ====
    print(part2(coords, rectangles))


if __name__ == "__main__":
    main()
