def create(lanternfish):
    new_lanternfish = [0] * 9
    for i, count in enumerate(lanternfish):
        new_lanternfish[(i - 1) % 9] = count
    new_lanternfish[6] += lanternfish[0]
    return new_lanternfish


lanternfish = [0] * 9
with open("day06/data") as f:
    for x in f.read().split(","):
        lanternfish[int(x)] += 1

# ==== PART 1 & 2 ====
for N in (80, 176):
    for _ in range(N):
        lanternfish = create(lanternfish)
    print(sum(lanternfish))
