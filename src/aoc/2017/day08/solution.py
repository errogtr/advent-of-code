from collections import defaultdict
from math import inf
from operator import add, eq, ge, gt, le, lt, ne, sub
from pathlib import Path


OP = {"inc": add, "dec": sub}


COND = {"<": lt, ">": gt, "<=": le, ">=": ge, "==": eq, "!=": ne}


def parse(instr: str):
    op_full, cond_full = instr.split(" if ")
    reg_x, op, x = op_full.split()
    reg_y, op_cond, y = cond_full.split()
    return reg_x, OP[op], int(x), reg_y, COND[op_cond], int(y)


def main(input_path: Path):
    with input_path.open() as f:
        data = f.read()

    registers = defaultdict(int)
    max_val = -inf
    for instr in data.splitlines():
        reg_x, op, x, reg_y, op_cond, y = parse(instr)
        if op_cond(registers[reg_y], y):
            registers[reg_x] = op(registers[reg_x], x)
        max_val = max(max_val, registers[reg_x])

    # ==== PART 1 ====
    print(max(registers.values()))

    # ==== PART 2 ====
    print(max_val)
