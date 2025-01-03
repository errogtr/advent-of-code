from math import ceil, floor
from statistics import median, mean


def triangular(n):
    return (n * (n + 1)) // 2


with open("day07/data") as f:
    crabs = [int(x) for x in f.read().split(",")]

# ==== PART 1 ====
m = median(crabs)
print(sum(abs(int(crab - m)) for crab in crabs))

# ==== PART 2 ====
mins = [floor(mean(crabs)), ceil(mean(crabs))]
print(min(sum(triangular(abs(crab - m)) for crab in crabs) for m in mins))
