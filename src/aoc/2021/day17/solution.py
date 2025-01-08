from itertools import product
from math import ceil, sqrt
from pathlib import Path
import re


def main(input_path: Path):
    with input_path.open() as f:
        x_min, x_max, y_min, y_max = map(int, re.findall(r"-*\d+", f.read()))

    # ==== PART 1 ====
    #
    # Considering only positive initial velocities, equations of motion are:
    #
    #    (1.1)   y_n = y_(n-1) - vy_(n-1) = n * y_0 - n * (n - 1) // 2
    #    (1.2)   vy_n = vy_(n-1) - 1 = vy_0 - n.
    #
    # This means that y_n = 0 iff n = 0 (initial time) or n = n_* := 2 * vy_0 + 1, for which
    #
    #    (2.2) vy_(n_*) = -v_0 - 1
    #    (2.3) y_(n_* + 1) = -v_0 - 1, since y_(n_*) = 0.
    #
    # The probe falls in the target area iff
    #
    #    (3)   y_(n_* + 1) >= y_min  <==(2.3)==>  vy_0 <= -y_min - 1.
    #
    # On the other hand, the highest point y_M is found when vy_n = 0 for a certain n, which leads to
    #
    #    (4)   y_M = vy_0 * (vy_0 + 1) // 2.
    #
    # Since (4) is monotonically increasing in vy_0, the maximum highest point is found at the upper
    # bound of inequality (3). Putting all together:
    #
    #    (sol.)  max(y_M) = (-y_min - 1) * (-y_min) // 2 = y_min * (y_min + 1) // 2

    print((y_min * (y_min + 1)) // 2)

    # ==== PART 2 ====
    #
    # Brute force approach, using lower and upper bounds for vx and vy (sub-optimal for sure...):
    #
    # - vx_0 <= x_max, otherwise it will fall outside target's x range at first step
    # - the sum of all x-steps before vx becomes 0 should not be less than x_min, this leads to:
    #
    #           vx_0 + (vx_0 - 1) + ... + 1 = vx_0 (vx_0 + 1) / 2 >= x_min
    #
    #   solving the quadratic equation and taking the positive root gives the lower bound
    #
    #           vx >= (-1 + sqrt(1 + 8 * x_min)) / 2
    #
    # - vy_0 >= y_min, otherwise it will fall outside target's y range at first step
    # - vy_0 < -y_min + 1, otherwise it will fall outside target's y range the step after y becomes 0

    vx_range = range(ceil((-1 + sqrt(1 + 8 * x_min)) / 2), x_max + 1)
    vy_range = range(y_min, -y_min)

    target = 0
    for vx, vy in product(vx_range, vy_range):
        x = 0
        y = 0
        while x <= x_max and y >= y_min:
            x += vx
            vx = max(vx - 1, 0)
            y += vy
            vy -= 1
            if x_min <= x <= x_max and y_min <= y <= y_max:
                target += 1
                break

    print(target)
