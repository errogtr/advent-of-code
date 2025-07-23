from copy import copy
import os
from pathlib import Path
from string import ascii_uppercase
from time import sleep


UP, RIGHT, DOWN, LEFT = [-1j, 1, 1j, -1]

TURNS = {UP: [RIGHT, LEFT], RIGHT: [UP, DOWN], DOWN: [RIGHT, LEFT], LEFT: [UP, DOWN]}


def main(input_path: Path):
    with input_path.open() as f:
        diagram_raw = f.read().splitlines()

    diagram = dict()
    z_start = None
    for y, row in enumerate(diagram_raw):
        for x, c in enumerate(row):
            diagram[x + y * 1j] = c
            if z_start is None and y == 0 and c == "|":
                z_start = x

    z, v_z = z_start, 1j
    line, letters, steps = "|", "", 0
    visited = {(z, v_z)}
    while line != " ":
        if line == "+":
            for v_nz in TURNS[v_z]:
                nz = z + v_nz
                if diagram[nz] != " " and (nz, v_nz) not in visited:
                    z, v_z = nz, v_nz
                    break
        else:
            z += v_z
            if line in ascii_uppercase:
                letters += line
        visited.add((z, v_z))
        line = diagram[z]
        steps += 1

    # ==== PART 1 ====
    print(letters)

    # ==== PART 2 ====
    print(steps)
