import re


def distance(time, speed, fly, rest):
    return speed * (fly * (time // (fly + rest)) + min(fly, time % (fly + rest)))


with open("data") as f:
    reindeers = [[int(x) for x in re.findall(r"\d+", l)] for l in f.read().splitlines()]


# ==== PART 1 ====
T = 2503
print(max(distance(T, s, f, r) for s, f, r in reindeers))

# ==== PART 2 ====
points = [0] * len(reindeers)
for t in range(1, T + 1):
    distances = [distance(t, s, f, r) for s, f, r in reindeers]
    points[distances.index(max(distances))] += 1
print(max(points))
