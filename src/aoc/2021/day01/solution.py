def sweep(data, idx):
    return sum(y > x for x, y in zip(data, data[idx:]))


with open("day01/data") as f:
    data = [int(line) for line in f.read().splitlines()]

# ==== PART 1 ====
print(sweep(data, 1))

# ==== PART 2 ====
print(sweep(data, 3))
