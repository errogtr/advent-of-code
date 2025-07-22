from copy import copy
from pathlib import Path


def solve(instructions, strange=False):
    curr = 0
    nex = instructions[curr]
    steps = 0
    while nex < len(instructions):
        nex = curr + instructions[curr]
        if strange and (instructions[curr] >= 3):
            instructions[curr] -= 1
        else:
            instructions[curr] += 1
        curr = nex
        steps += 1
    return steps


def main(input_path: Path):
    with input_path.open() as f:
        instructions = [int(x) for x in f.readlines()]


    # ==== PART 1 ====
    print(solve(copy(instructions)))

    # ==== PART 2 ====
    print(solve(copy(instructions), strange=True))
