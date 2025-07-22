from pathlib import Path
import math


# Helper function to generate points along the perimeter of the square
def get_square_perimeter(k):
    """Generate the points around the perimeter of a square with side length 2*k."""
    perimeter = list()
    start = (k, k)

    # Define the four directions for the sides of the square: right, up, left, down
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # (dx, dy)

    for dx, dy in directions:
        x, y = start
        for _ in range(2 * k):
            start = (x + dx, y + dy)
            perimeter.append(start)
            x, y = start

    return perimeter


def adj(x, y):
    """Return the adjacent positions of a given point (x, y)."""
    return [
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
    ]


def get_spiral(N):
    """Generate values in a spiral pattern until we reach or exceed N."""
    spiral = {(0, 0): 1}
    k = 1

    # Generate spiral by iterating over concentric square layers
    while True:
        for p in get_square_perimeter(k):
            val = sum(spiral.get(q, 0) for q in adj(*p))
            if val >= N:
                return val
            spiral[p] = val
        k += 1


def distance(N):
    """Compute the Manhattan distance to the given position of N in the spiral."""
    k = int(math.sqrt(N))
    l = k - (1 - k % 2)  # Adjust k for odd-length square

    # Find position in the square by checking the specific perimeter
    x, y = next(
        p for i, p in enumerate(get_square_perimeter(l // 2 + 1), l**2 + 1) if i == N
    )

    return abs(x) + abs(y)


def main(input_path: Path):
    with input_path.open() as f:
        N = int(f.read())

    # ==== PART 1 ====
    print(distance(N))

    # ==== PART 2 ====
    print(get_spiral(N))
