from collections import defaultdict
from itertools import combinations
from math import inf, sqrt
import re



def parse(data):
    return [int(x) for x in re.findall(r"-*\d+", data)]


def main(input_path):
    with input_path.open() as f:
        particles = [parse(data) for data in f.read().splitlines()]

    acc = [abs(a_x) + abs(a_y) + abs(a_z) for *_, a_x, a_y, a_z in particles]
    slow, _ = min(enumerate(acc), key=lambda x: x[1])
    print(slow)

    collisions = defaultdict(set)
    for (i1, p1), (i2, p2) in combinations(enumerate(particles), 2):
        if p1 == p2:
            pass
        x1, y1, z1, v_x1, v_y1, v_z1, a_x1, a_y1, a_z1 = p1
        x2, y2, z2, v_x2, v_y2, v_z2, a_x2, a_y2, a_z2 = p2
        A_x, A_y, A_z = (x2 - x1), (y2 - y1), (z2 - z1)
        B_x, B_y, B_z = (
            (v_x2 - v_x1 + (a_x2 - a_x1) / 2),
            (v_y2 - v_y1 + (a_y2 - a_y1) / 2),
            (v_z2 - v_z1 + (a_z2 - a_z1) / 2),
        )
        C_x, C_y, C_z = (a_x2 - a_x1) / 2, (a_y2 - a_y1) / 2, (a_z2 - a_z1) / 2

        delta_x = B_x**2 - 4 * A_x * C_x
        if delta_x < 0:
            continue
        delta_y = B_y**2 - 4 * A_y * C_y
        if delta_y < 0:
            continue
        delta_z = B_z**2 - 4 * A_z * C_z
        if delta_z < 0:
            continue

        t_x, t_y, t_z = inf, inf, inf
        if A_x != 0:
            t_x_pos = (-B_x + sqrt(delta_x)) / (2 * A_x)
            t_x_neg = (-B_x - sqrt(delta_x)) / (2 * A_x)
            t_x_min, t_x_max = min(t_x_pos, t_x_neg), max(t_x_pos, t_x_neg)
            t_x = t_x_min if t_x_min > 0 else t_x_max
        elif B_x != 0:
            t_x = -C_x / B_x
        else:
            continue

        if t_x <= 0 or t_x != int(t_x):
            continue

        if A_y != 0:
            t_y_pos = (-B_y + sqrt(delta_y)) / (2 * A_y)
            t_y_neg = (-B_y - sqrt(delta_y)) / (2 * A_y)
            t_y_min, t_y_max = min(t_y_pos, t_y_neg), max(t_y_pos, t_y_neg)
            t_y = t_y_min if t_y_min > 0 else t_y_max
        elif B_y != 0:
            t_y = -C_y / B_y
        else:
            continue

        if t_y == int(t_y):
            pass

        if A_z != 0:
            t_z_pos = (-B_z + sqrt(delta_z)) / (2 * A_z)
            t_z_neg = (-B_z - sqrt(delta_z)) / (2 * A_z)
            t_z_min, t_z_max = min(t_z_pos, t_z_neg), max(t_z_pos, t_z_neg)
            t_z = t_z_min if t_z_min > 0 else t_z_max
        elif B_z != 0:
            t_z = -C_z / B_z
        else:
            continue

        print(t_x, t_y, t_z)

        if (
            t_x == t_y == t_z and t_x > 0
        ):  # or (t_x == inf and t_y == t_z) or (t_y == inf and t_x == t_z) or (t_z == inf and t_x == t_y) or (t_x == t_y == inf) or (t_x == t_z == inf) or (t_y == t_z == inf):
            print(t_x)
            collisions[t_x] |= {i1, i2}

    removed = {i: False for i in range(len(particles))}
    for t, collided in sorted(collisions.items()):
        remaining = [p for p in collided if not removed[p]]
        if len(remaining) > 1:
            for i in remaining:
                removed[i] = True
    print(sum(not r for r in removed.values()))
