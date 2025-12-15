DIRECTIONS = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}


def key(instructions, keypad, x, y):
    code = ""
    for line in instructions:
        for c in line:
            vx, vy = DIRECTIONS[c]
            if (digit := (x + vx, y + vy)) in keypad:
                x, y = digit
        code += keypad[(x, y)]
    return code


with open("data") as f:
    instructions = f.read().splitlines()

# ==== PART 1 ====
square = {
    (-1, 1): "1",
    (0, 1): "2",
    (1, 1): "3",
    (-1, 0): "4",
    (0, 0): "5",
    (1, 0): "6",
    (-1, -1): "7",
    (0, -1): "8",
    (1, -1): "9",
}
print(key(instructions, square, 0, 0))


# ==== PART 2 ====
star = {
    (0, 2): "1",
    (-1, 1): "2",
    (0, 1): "3",
    (1, 1): "4",
    (-2, 0): "5",
    (-1, 0): "6",
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (-1, -1): "A",
    (0, -1): "B",
    (1, -1): "C",
    (0, -2): "D",
}
print(key(instructions, star, -2, 0))
