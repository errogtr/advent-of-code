from heapq import heappop, heappush


def nn(x, y):
    return [
        (a, b)
        for a, b in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
        if a >= 0 and b >= 0
    ]


def is_wall(x, y, favorite):
    return bin(x * x + 3 * x + 2 * x * y + y + y * y + favorite).count("1") % 2


with open("data") as f:
    favorite = int(f.read())

steps, current, target = 0, (1, 1), (31, 39)
state = (steps, current)
queue = [state]
visited = {state}
while queue:
    steps, current = heappop(queue)

    if current == target:
        break

    for pos in nn(*current):
        state = (steps + 1, pos)
        if not is_wall(*pos, favorite) and state not in visited:
            visited.add(state)
            heappush(queue, state)

# ==== PART 1 ====
print(steps)

# ==== PART 2 ====
# works because for my input steps is > 50 and by construction
# heapqueue already exhausted all visited position with at most 50 steps
print(len({pos for steps, pos in visited if steps <= 50}))
