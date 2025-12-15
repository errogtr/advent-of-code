import re
from itertools import product


def parse(instruction):
    direction, idx, shift = re.search(r"(x|y)=(\d+) by (\d+)", instruction).groups()
    return direction, int(idx), int(shift)


def rotate(row, shift, length):
    return row[-shift:] + row[: length - shift]


with open("data") as f:
    instructions = f.read().splitlines()

Lx, Ly = 50, 6
display = [["."] * Lx for _ in range(Ly)]

# ==== PART 1 ====
for instruction in instructions:
    if instruction.startswith("rect"):
        max_x, max_y = map(int, instruction[5:].split("x"))
        for x, y in product(range(max_x), range(max_y)):
            display[y][x] = "#"
    else:  # rotate
        direction, idx, shift = parse(instruction)
        if direction == "x":
            rotated = rotate([row[idx] for row in display], shift, Ly)
            display = [
                [rotated[y] if x == idx else v for x, v in enumerate(row)]
                for y, row in enumerate(display)
            ]
        else:
            display[idx] = rotate(display[idx], shift, Lx)
print(sum(sum(v == "#" for v in row) for row in display))

# ==== PART 2 ====
print("\n".join("".join(row) for row in display))
