from itertools import combinations
import re


def parse_node(line):
    x, y, size, used, avail, use_perc = map(int, re.findall(r"\d+", line))
    return (x, y), (size, used, avail, use_perc)


with open("data") as f:
    nodes = dict(parse_node(l) for l in f.read().splitlines()[2:])

viable = 0
for A, B in combinations(nodes.values(), 2):
    _, used_A, avail_A, _ = A
    _, used_B, avail_B, _ = B
    if 0 < used_A <= avail_B:
        viable += 1
    if 0 < used_B <= avail_A:
        viable += 1
print(viable)
