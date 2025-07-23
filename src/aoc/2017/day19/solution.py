from copy import copy
import os
from pathlib import Path
from string import ascii_uppercase
from time import sleep


UP, RIGHT, DOWN, LEFT = [(0, -1), (1, 0), (0, 1), (-1, 0)]

TURNS = {
    UP: [RIGHT, LEFT],
    RIGHT: [UP, DOWN],
    DOWN: [RIGHT, LEFT],
    LEFT: [UP, DOWN]
}


def main(input_path: Path):
    with input_path.open() as f:
        diagram_raw = f.read().splitlines()
    
    lx = len(diagram_raw[0])
    ly = len(diagram_raw)

    diagram = dict()
    for y, row in enumerate(diagram_raw):
        for x, c in enumerate(row):
            diagram[(x, y)] = c
    
    x, y = next(i for i in range(lx) if diagram[(i, 0)] == "|"), 0
    vx, vy = 0, 1
    line, letters, steps = "|", "", 0
    visited = [(x, y, vx, vy)]
    while line != " ":
        if line == "+":
            for vnx, vny in TURNS[(vx, vy)]:
                nx, ny = x + vnx, y + vny
                if diagram[(nx, ny)] != " " and (nx, ny, vnx, vny) not in visited:
                    x, y, vx, vy = nx, ny, vnx, vny
                    break
        else:
            x, y = x + vx, y + vy
            if line in ascii_uppercase:
                letters += line
        visited.append((x, y, vx, vy))
        line = diagram[(x, y)]
        steps += 1

    # ==== PART 1 ====
    print(letters)

    # ==== PART 2 ====
    print(steps)