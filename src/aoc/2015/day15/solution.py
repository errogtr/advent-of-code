import re
from itertools import combinations
from math import prod


def spoons(N, k):
    """k-partitions of N -> equivalent to stars and bars problem"""
    for splits in combinations(range(N - 1), k - 1):
        yield [b - a for a, b in zip((-1,) + splits, splits + (N-1,))]


def score(X, I):
    return prod(
        max(0, sum(x * a for x, a in zip(X, alpha)))
        for alpha in zip(*(i[:-1] for i in I))
    )


with open("data") as fp:
    ingredients = [
        [int(x) for x in re.findall(r"-*\d+", l)] for l in fp.read().splitlines()
    ]

S = 100
# ==== PART 1 ====
print(max(score(X, ingredients) for X in spoons(S, len(ingredients))))

# ==== PART 2 ====
print(
    max(
        score(X, ingredients)
        for X in spoons(S, len(ingredients))
        if sum(s * i[-1] for s, i in zip(X, ingredients)) == 500
    )
)
