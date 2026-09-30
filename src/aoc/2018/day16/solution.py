from copy import copy
from itertools import cycle
import re
import click
from aoc.utils import read_data, timer


def addr(a, b, r): return r[a] + r[b]
def addi(a, b, r): return r[a] + b
def mulr(a, b, r): return r[a] * r[b]
def muli(a, b, r): return r[a] * b
def banr(a, b, r): return r[a] & r[b]
def bani(a, b, r): return r[a] & b
def borr(a, b, r): return r[a] | r[b]
def bori(a, b, r): return r[a] | b
def setr(a, b, r): return r[a]
def seti(a, b, r): return a
def gtir(a, b, r): return int(a > r[b])
def gtri(a, b, r): return int(r[a] > b)
def gtrr(a, b, r): return int(r[a] > r[b])
def eqir(a, b, r): return int(a == r[b])
def eqri(a, b, r): return int(r[a] == b)
def eqrr(a, b, r): return int(r[a] == r[b])


def execute(op, a, b, c, reg):
    out = copy(reg)
    out[c] = op(a, b, reg)
    return out

# fmt: off
OPS = [
    addr, addi, mulr, muli, 
    banr, bani, borr, bori, 
    setr, seti, gtir, gtri, 
    gtrr, eqir, eqri, eqrr
    ]
# fmt: on


def parse(sample):
    nums = [int(x) for x in re.findall(r"\d+", sample)]
    before = nums[:4]
    opcode, a, b, c = nums[4:8]
    after = nums[8:]
    return opcode, a, b, c, before, after



@timer
def part1(data):
    samples = data.split("\n\n\n\n")[0]
    op_matches = 0
    for sample in samples.split("\n\n"):
        _, a, b, c, before, after = parse(sample)
        op_matches += sum(execute(op, a, b, c, before) == after for op in OPS) >= 3
    return op_matches


@timer
def part2(data):
    samples, program = data.split("\n\n\n\n")
    op_sampling = [set(OPS) for _ in range(len(OPS))]
    for sample in samples.split("\n\n"):
        opcode, a, b, c, before, after = parse(sample)
        op_sampling[opcode] &= {op for op in OPS if execute(op, a, b, c, before) == after}

    # Resolve for opcode samples that are associated with more than one operation
    # Assumption: at least one opcode owns one and only one operation.
    # For a more general case, Kuhn's algorithm must be chosen 
    for i in cycle(range(len(op_sampling))):
        if len(op_sampling[i]) == 1:
            for j in range(len(op_sampling)):
                if j != i:
                    op_sampling[j] -= op_sampling[i]

        if all(len(ops) == 1 for ops in op_sampling):
            break

    ops_mapping = [ops.pop() for ops in op_sampling]
    registers = [0] * 4
    for instr in program.splitlines():
        opcode, a, b, c = map(int, instr.split())
        registers = execute(ops_mapping[opcode], a, b, c, registers)

    return registers[0]


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2(data))


if __name__ == "__main__":
    main()
