from collections import defaultdict
from itertools import batched, zip_longest
import re


def cloud_lines(coords, skip_diag=True):
    clouds = defaultdict(int)
    for x1, y1, x2, y2 in batched(coords, 4):
        if skip_diag and x1 != x2 and y1 != y2:
            continue

        lx, ly = abs(x2 - x1), abs(y2 - y1)
        dx = (x2 - x1) // lx if lx else 0
        dy = (y2 - y1) // ly if ly else 0

        for s, t in zip_longest(range(lx + 1), range(ly + 1), fillvalue=0):
            clouds[(x1 + s * dx, y1 + t * dy)] += 1

    return clouds.values()


with open("day05/data") as f:
    coords = [int(x) for x in re.findall(r"\d+", f.read())]

# ==== PART 1 ====
print(sum(count > 1 for count in cloud_lines(coords)))

# ==== PART 2 ====
print(sum(count > 1 for count in cloud_lines(coords, skip_diag=False)))
