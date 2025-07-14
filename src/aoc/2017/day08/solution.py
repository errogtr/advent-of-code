from collections import defaultdict
from math import inf
from operator import add, eq, ge, gt, le, lt, ne, sub
from pathlib import Path


OPS = {"inc": add, "dec": sub}


COND = {"<": lt, ">": gt, "<=": le, ">=": ge, "==": eq, "!=": ne}


def main(input_path: Path):
    with input_path.open() as f:
        data = f.read()

    registers = defaultdict(int)
    max_val = -inf
    for instr in data.splitlines():
        reg_x, op, x, _, reg_y, op_cond, y = instr.split()
        if COND[op_cond](registers[reg_y], int(y)):
            registers[reg_x] = OPS[op](registers[reg_x], int(x))
        max_val = max(max_val, registers[reg_x])

    # ==== PART 1 ====
    print(max(registers.values()))

    # ==== PART 2 ====
    print(max_val)
