from collections import defaultdict


def visit(house, step, max_range, mult):
    for j in range(step, max_range, step):
        house[j] += mult * step


with open("data") as f:
    target = int(f.read())

# ==== PART 1 ====
house = defaultdict(int)
for i in range(1, (target // 10) + 1):
    visit(house, i, (target // 10) + 1, 10)
print(next(k for k, v in house.items() if v >= target))


# ==== PART 2 ====
house = defaultdict(int)
for i in range(1, (target // 10) + 1):
    visit(house, i, 51 * i, 11)
print(next(k for k, v in house.items() if v >= target))
