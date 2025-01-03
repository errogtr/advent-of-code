from collections import defaultdict
from itertools import permutations, pairwise


distances = defaultdict(dict)
with open("data") as f:
    for line in f.read().splitlines():
        nodes, d = line.split(" = ")
        u, v = nodes.split(" to ")
        distances[u] |= {v: int(d)}
        distances[v] |= {u: int(d)}

lengths = [
    sum(distances[src][dst] for src, dst in pairwise(path))
    for path in permutations(distances)
]

# ==== PART 1 ====
print(min(lengths))

# ==== PART 2 ====
print(max(lengths))
