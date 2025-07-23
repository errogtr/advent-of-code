from collections import defaultdict
from pathlib import Path


def get_val(raw, reg):
    if raw.isalpha():
        return reg[raw]
    return int(raw)


def exec(instructions, sound_on=False):
    regs = [defaultdict(int), defaultdict(int) | {"p": 1}]
    queues = [list(), list()]
    curr = [0, 0]
    id = 0
    counter = 0
    while True:
        cmd, *args = instructions[curr[id]].split()
        match cmd:
            case "set":
                regs[id][args[0]] = get_val(args[1], regs[id])
            case "add":
                regs[id][args[0]] += get_val(args[1], regs[id])
            case "mul":
                regs[id][args[0]] *= get_val(args[1], regs[id])
            case "mod":
                regs[id][args[0]] %= get_val(args[1], regs[id])
            case "snd":
                queues[1 - id].append(regs[id][args[0]])
                counter += id == 1
            case "rcv":
                if sound_on:
                    return queues[1 - id][-1]
                if queues[id]:
                    regs[id][args[0]] = queues[id].pop(0)
                elif queues[1 - id]:
                    id ^= 1
                    curr[id] -= 1
                else:
                    return counter
            case "jgz":
                if get_val(args[0], regs[id]) > 0:
                    curr[id] += get_val(args[1], regs[id]) - 1
        curr[id] += 1


def main(input_path: Path):
    with input_path.open() as f:
        instructions = f.read().splitlines()

    # ==== PART 1 ====
    print(exec(instructions, sound_on=True))

    # ==== PART 2 ====
    print(exec(instructions))
