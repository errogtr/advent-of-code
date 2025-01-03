from itertools import combinations


with open("data") as f:
    containers = [int(x) for x in f.read().splitlines()]

# ==== PART 1 ====
combs = [
    len([c for c in combinations(containers, i) if sum(c) == 150])
    for i in range(2, len(containers) + 1)
]
print(sum(combs))

# ==== PART 2 ====
print(next(c for c in combs if c))
