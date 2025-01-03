import re
from collections import defaultdict
from itertools import permutations, pairwise


def max_happiness(happiness):
    return max(
        sum(happiness[n][m] + happiness[m][n] for n, m in pairwise(table + (table[0],)))
        for table in permutations(happiness)
    )


happiness = defaultdict(dict)
with open("data") as f:
    for line in f.read().splitlines():
        name, sign, units, neighbor = re.match(
            r"(\w+).*(gain|lose)\s(\d+).*\s(\w+)", line
        ).groups()
        happiness[name] |= {neighbor: (-1) ** (sign == "lose") * int(units)}


# ==== PART 1 ====
print(max_happiness(happiness))

# ==== PART 2 ====
for name in list(happiness):
    happiness["Me"][name] = happiness[name]["Me"] = 0
print(max_happiness(happiness))
