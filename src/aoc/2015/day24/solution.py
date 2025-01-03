from itertools import combinations
from math import prod


def entanglements(nums, s):
    for k in range(1, len(nums)):
        if qe := min([prod(c) for c in combinations(nums, k) if sum(c) == s], default=0):
            return qe


with open("data") as f:
    nums = [int(x) for x in f.readlines()]


# ==== PART 1 ====
print(entanglements(nums, sum(nums) // 3))

# ==== PART 2 ====
print(entanglements(nums, sum(nums) // 4))
