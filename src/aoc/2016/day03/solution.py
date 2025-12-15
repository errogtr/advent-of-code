def is_possible(a, b, c):
    return a + b > c


with open("data") as f:
    triangles = [[int(x) for x in line.split()] for line in f.read().splitlines()]

# ==== PART 1 ====
print(sum(is_possible(*sorted(t)) for t in triangles))

# ==== PART 2 ====
print(
    sum(
        sum(is_possible(*sorted(t)) for t in zip(*triangles[i:i + 3]))
        for i in range(0, len(triangles), 3)
    )
)
