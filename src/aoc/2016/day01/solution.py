from itertools import pairwise


N, S, W, E = "N", "S", "W", "E"

with open("data") as f:
    document = f.read().split(", ")

visited = [(0, 0)]
previous = N
for instruction in document:
    x, y = visited[-1]
    direction, steps = instruction[0], int(instruction[1:])
    if previous == N:
        x, previous = (x + steps, W) if direction == "R" else (x - steps, E)
    elif previous == S:
        x, previous = (x - steps, E) if direction == "R" else (x + steps, W)
    elif previous == W:
        y, previous = (y + steps, S) if direction == "R" else (y - steps, N)
    else:
        y, previous = (y - steps, N) if direction == "R" else (y + steps, S)
    visited.append((x, y))
print(sum(abs(t) for t in visited[-1]))

blocks = list()
for (x, y), (z, w) in pairwise(visited):
    if y == w:
        for a in range(x, z, (-1) ** (x > z)):
            if (a, y) in blocks:
                print(abs(a) + abs(y))
                break
            blocks.append((a, y))
    if x == z:
        for a in range(y, w, (-1) ** (y > w)):
            if (x, a) in blocks:
                print(abs(x) + abs(a))
                break
            blocks.append((x, a))