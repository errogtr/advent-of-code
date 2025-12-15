from itertools import pairwise

with open("data") as f:
    blacklist = [[int(x) for x in pair.split("-")] for pair in f.readlines()]

blocked = list()
for a, b in sorted(blacklist):
    if not blocked:
        blocked.append((a, b))
    else:
        c, d = blocked[-1]
        if a <= d+1 <= b:
            blocked[-1] = (c, b)
        elif d < a:
            blocked.append((a, b))

# ==== PART 1 ====
print(next(b + 1 for (_, b), (c, _) in pairwise(blocked) if c - b > 1))

# ==== PART 2 ====
print(sum(c - b - 1 for (_, b), (c, _) in pairwise(blocked)))
