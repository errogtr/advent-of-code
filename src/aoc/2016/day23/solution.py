from math import factorial
import click
from aoc.utils import read_data, timer


def assembunny(a: int, c: int, d: int) -> int:
    """
    Compute the result of the assembunny code.

    The instructions implement: factorial(a) + c * d
    """
    return factorial(a) + c * d


def extract_register(instruction: str) -> int:
    """Extract the numeric value from a 'cpy/jnz <value> <register>' instruction."""
    return int(instruction.split()[1])


@timer
def part1(c: int, d: int) -> int:
    """Compute factorial(7) + c * d."""
    return assembunny(7, c, d)


@timer
def part2(c: int, d: int) -> int:
    """
    Compute factorial(12) + c * d.

    Running the simulation for a=12 would take ~479 million iterations,
    so we use the closed-form solution instead.
    """
    return assembunny(12, c, d)


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)
    instructions = data.splitlines()

    # Extract input-specific constants c and d from instructions
    c = extract_register(instructions[19])
    d = extract_register(instructions[20])

    # ==== PART 1 ====
    print(part1(c, d))

    # ==== PART 2 ====
    print(part2(c, d))


if __name__ == "__main__":
    main()


# ============================================================================
# Original simulation code (preserved for reference)
# ============================================================================
# This was the initial solution before discovering the factorial pattern.
#
# def get_value(arg: str, registers: dict) -> int:
#     return registers[arg] if arg.isalpha() else int(arg)
#
# def apply_toggle(cmd: str) -> str:
#     toggle_map = {
#         "inc": "dec",
#         "dec": "inc",
#         "tgl": "inc",
#         "jnz": "cpy",
#         "cpy": "jnz"
#     }
#     return toggle_map[cmd]
#
# def simulate(instructions: list[str], registers: dict) -> int:
#     instructions = instructions.copy()
#     pc = 0
#     while pc < len(instructions):
#         parts = instructions[pc].split()
#         cmd, args = parts[0], parts[1:]
#         match cmd:
#             case "cpy":
#                 if args[1].isalpha():
#                     registers[args[1]] = get_value(args[0], registers)
#             case "inc":
#                 registers[args[0]] += 1
#             case "dec":
#                 registers[args[0]] -= 1
#             case "jnz":
#                 if get_value(args[0], registers) != 0:
#                     offset = get_value(args[1], registers)
#                     pc += offset
#                     continue
#             case "tgl":
#                 offset = get_value(args[0], registers)
#                 target = pc + offset
#                 if 0 <= target < len(instructions):
#                     target_parts = instructions[target].split()
#                     toggled_cmd = apply_toggle(target_parts[0])
#                     instructions[target] = f"{toggled_cmd} {' '.join(target_parts[1:])}"
#         pc += 1
#     return registers["a"]
